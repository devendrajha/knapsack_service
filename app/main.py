from flask import Flask, request
from flask import jsonify
from app.custom_errors.insufficien_data_found_exception import InsufficientDataFound, BothListSizesNotMatch
from app.logging.logger import yield_logger
from app.service.knapsack_optimizer_impl import KnapsackOptimizer
from app.model.knapsack_value_obj import KnapsackVo
import logging as log

from app.util.status_code_enum import ResponseCodeEnum

app = Flask(__name__)
log = yield_logger()

@app.route('/')
def kaas():
    """Return a HTTP greeting."""
    res = 'For knapsack calculation please change at route: /knapsack'
    log.info(res)
    return res


@app.route('/knapsack', methods=['POST'])
def knap_service():
    """ knapsack service """
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            log.debug(json)
            vo = KnapsackVo()
            vo.weight = json['weights']
            vo.values = json['values']
            vo.container = json['capacities']

            proc = KnapsackOptimizer(vo)
            result = proc.optimize_maximum()
            log.debug('result', result)
            return jsonify({"result": result}), ResponseCodeEnum.SUCCESS.value
        else:
            return 'Content-Type not supported!'

    except BothListSizesNotMatch as e:
        error = f"both list data {json['weights']} and {json['values']} should be same length"
        return error, ResponseCodeEnum.INVALID.value
    except InsufficientDataFound as e:
        error = 'both input list are empty'
        return error
    except KeyError as e:
        sample = {
            "weights": [15, 10, 2, 4],
            "values": [30, 25, 2, 16],
            "capacities": 42
        }
        error = f'Please provide proper data for example {sample}'
        return error, ResponseCodeEnum.BAD_REQUEST.value
    except TypeError as e:
        error = f'Please provide integer value in input data'
        return error, ResponseCodeEnum.BAD_REQUEST.value

