# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
import os
from typing import Optional

from dotenv import dotenv_values
from pydantic import BaseModel, Field


class ConfigModel(BaseModel):
    EMBEDDING_MODEL: str = Field(description="Embedding模型")
    RERANK_MODEL: str = Field(description="Rerank模型")
    DEVICE: str = Field(description="运行在哪种设备中")
    MODEL_BASE_DIR: str = Field(description="模型默认路径")
    # FastAPI
    UVICORN_IP: str = Field(description="FastAPI监听地址")
    UVICORN_PORT: int = Field(description="FastAPI监听端口", default=8001)
    SSL_ENABLE: Optional[str] = Field(description="选择是否开启SSL", default=None)
    SSL_CERTFILE: Optional[str] = Field(description="SSL证书路径", default=None)
    SSL_KEYFILE: Optional[str] = Field(description="SSL私钥路径", default=None)
    SSL_KEY_PWD: Optional[str] = Field(description="SSL私钥密码", default=None)
    # Logging
    LOG: str = Field(description="日志记录模式")


class Config:
    config: ConfigModel

    def __init__(self):
        if os.getenv("CONFIG"):
            config_file = os.getenv("CONFIG")
        else:
            config_file = "./config/.env"
        self.config = ConfigModel(**(dotenv_values(config_file)))

        if os.getenv("PROD"):
            os.remove(config_file)

    def __getitem__(self, key):
        if key in self.config.__dict__:
            return self.config.__dict__[key]
        else:
            return None


config = Config()