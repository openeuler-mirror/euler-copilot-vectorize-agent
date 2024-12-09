# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.

from typing import List
from langchain.embeddings import HuggingFaceBgeEmbeddings

from vectorize_agent.config import config


class VectorModel:
    def __init__(
            self
    ):
        """
        :param embedding_model:     模型地址
        :param embedding_device:    运行设备
        :return:
        """
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name=config['MODEL_BASE_DIR'] + config['EMBEDDING_MODEL'],
            model_kwargs={'device': config['DEVICE']}
        )
        self.embedding_function = self.embeddings.embed_documents


vector_model = VectorModel()


def embedding(texts: List[str]) -> List[List[float]]:
    embedding_function = vector_model.embedding_function
    embeddings = embedding_function(texts)
    if type(embeddings) != list:
        embeddings = embeddings.tolist()
    return embeddings
