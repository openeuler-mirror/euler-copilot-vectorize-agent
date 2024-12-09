# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
import fastapi
import uvicorn

from vectorize_agent.logger import log_config
from vectorize_agent.rerank.reranking import reranking
from vectorize_agent.vectorize.embedding import embedding
from vectorize_agent.app.models import EmbeddingReq, RerankingReq
from vectorize_agent.config import config

app = fastapi.FastAPI()


@app.get('/health_check/ping')
def ping() -> str:
    return "pong"


@app.post('/embedding')
def embed(req: EmbeddingReq):
    return embedding(req.texts)


@app.post('/reranking')
def rerank(req: RerankingReq):
    return reranking(req)


def main():
    if config["SSL_ENABLE"]:
        uvicorn.run(app, host=config["UVICORN_IP"], port=int(config["UVICORN_PORT"]), log_config=log_config,
                    ssl_certfile=config["SSL_CERTFILE"], ssl_keyfile=config["SSL_KEYFILE"],
                    ssl_keyfile_password=config["SSL_KEY_PWD"])
    else:
        uvicorn.run(app, host=config["UVICORN_IP"], port=int(config["UVICORN_PORT"]),
                    log_config=log_config)


if __name__ == '__main__':
    main()
