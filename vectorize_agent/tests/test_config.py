# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from fastapi.testclient import TestClient

from vectorize_agent.app.app import app

test_client = TestClient(app=app)
