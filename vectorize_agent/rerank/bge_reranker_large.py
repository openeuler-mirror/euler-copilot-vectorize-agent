# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from typing import List, Sequence, Optional

from langchain.schema import Document
from langchain.pydantic_v1 import Extra
from langchain_core.callbacks import Callbacks
from sentence_transformers import CrossEncoder
from langchain.retrievers.document_compressors.base import BaseDocumentCompressor
from vectorize_agent.config import config


class BgeRerankerLargeModel(BaseDocumentCompressor):
    """Model name to use for reranking."""
    model_name: str = config['MODEL_BASE_DIR']+config['RERANK_MODEL']
    """Number of documents to return."""
    top_n: int = 5
    """CrossEncoder instance to use for reranking."""
    model: CrossEncoder = CrossEncoder(model_name, device=config["DEVICE"])

    def rerank(self, query, docs):
        model_inputs = [[query, doc] for doc in docs]
        scores = self.model.predict(model_inputs)
        results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return results

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid
        arbitrary_types_allowed = True

    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None
    ) -> List[Document]:
        """
        Compress documents using reranker models.

        Args:
            documents: A sequence of documents to compress.
            query: The query to use for compressing the documents.
            callbacks: Callbacks to run during the compression process.

        Returns:
            A sequence of compressed documents.
        """
        if len(documents) == 0:  # to avoid empty call
            return []
        _docs = [d for d in documents]
        results = self.rerank(query, _docs)
        final_results = []
        for r in results:
            doc = documents[r[0]]
            final_results.append(doc)
        return final_results


bge_reranker_large_model = BgeRerankerLargeModel()
