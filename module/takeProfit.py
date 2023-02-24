from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging
from variables import globalVar
from binanceAPI.teleBot import sendData
from components.fixOrder import *

#config_logging(logging, logging.DEBUG)

# TAKE PROFIT
def takeProfit(symbol,positionSide,side,type,stopPrice): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            stopPrice = float(round(stopPrice,globalVar.decimalPrecision)),
            timeInForce = "GTC",
            closePosition = "true",
        )
        #logging.info(response)
    except ClientError as error:
        sendData("TakeProfit error. Error code: {}, error message: {}".format(error.error_code, error.error_message))
        if error.error_code == -2021:
            prRed("ERROR:: Order Imme Trigger | Type: takeProfit")