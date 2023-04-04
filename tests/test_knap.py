# pylint: disable=protected-access, missing-class-docstring, missing-function-docstring
import logging
import pytest
from app.service.knapsack_optimizer_impl import KnapsackOptimizer
import json

from app.main import app
from app.custom_errors.insufficien_data_found_exception import InsufficientDataFound, BothListSizesNotMatch

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'For knapsack calculation please change at route: /knapsack'


def test_knap_failure_test_1():
    payload = json.dumps({})
    response = app.test_client().post('/knapsack', headers={"Content-Type": "application/json"}, data=payload)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Please provide proper data for example {'weights': [15, 10, 2, 4], 'values': [30, 25, 2, 16], 'capacities': 42}"

def test_knap_failure_test_2():
    payload = json.dumps({
        "values": [],
        "weights": [10, 20, 30],
        "capacities": 50
        })
    response = app.test_client().post('/knapsack', headers={"Content-Type": "application/json"}, data=payload)
    assert response.status_code == 403
    assert response.data.decode('utf-8') == "both list data [10, 20, 30] and [] should be same length"

def test_knap_failure_test_3():
    payload = json.dumps({
        "values": [60, 100, 120],
        "weights": [10, 20, 30],
        "capacities": "50"
        })
    response = app.test_client().post('/knapsack', headers={"Content-Type": "application/json"}, data=payload)
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Please provide integer value in input data"

