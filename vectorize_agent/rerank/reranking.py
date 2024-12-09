# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from __future__ import annotations
from vectorize_agent.app.models import RerankingReq

from vectorize_agent.rerank.bge_reranker_large import bge_reranker_large_model


def reranking(req: RerankingReq):
    sort_res = bge_reranker_large_model.compress_documents(req.documents, req.raw_question)
    return sort_res[:req.top_k]
