from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging, json
from variables import globalVar
from binanceAPI.teleBot import sendData
from components.fixOrder import *

# config_logging(logging, logging.DEBUG)

def getPositionPrice(symbol, positionSide):
    try:
        response = um_futures_client.get_position_risk(recvWindow=6000)
        # print(json.dumps(response, indent = 4))
        for i in response:
            if i["symbol"] == symbol and i["positionSide"] == positionSide:
                price = i["entryPrice"]
                return float(price)
                #print(json.dumps(i, indent = 4))

    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

