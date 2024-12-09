# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from vectorize_agent.tests.test_config import test_client


def test_embedding():
    res = test_client.post("/embedding", json={"texts": ["你好"]})
    res_json = res.json()
    assert len(res_json) == 1
    assert len(res_json[0]) == 1024
    assert res.status_code == 200
