# Copyright (c) Huawei Technologies Co., Ltd. 2023-2024. All rights reserved.
from vectorize_agent.tests.test_config import test_client


def test_reranking():
    top_k = 3
    body = {
        'documents': [
            (22, '今天的天气下雨了'),
            (78, '是一个操作系统'),
            (13, '没人知道'),
            (99, 'openEuler是一个操作系统'),
            (56, 'openEuler由华为主导研发')
        ],
        'raw_question': '介绍一下openEuler',
        'top_k': top_k
    }
    res = test_client.post("/reranking", json=body)
    res_json = res.json()
    assert len(res_json) == top_k
    assert res.status_code == 200
