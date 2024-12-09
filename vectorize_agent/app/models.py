# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from typing import List, Optional

from pydantic import BaseModel

from vectorize_agent.config import config


class EmbeddingReq(BaseModel):
    texts: List[str]


class RerankingReq(BaseModel):
    documents: List
    raw_question: str
    top_k: int
    model_name: Optional[str] = config['RERANK_MODEL']
