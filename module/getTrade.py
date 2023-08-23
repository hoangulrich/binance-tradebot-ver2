#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError
from binanceAPI.user import um_futures_client
from variables import globalVar

def getTradeStart(symbol):
    response = um_futures_client.get_account_trades(symbol=symbol, recvWindow=6000)
    return len(response)

def getTradeEnd(symbol):
    response = um_futures_client.get_account_trades(symbol=symbol, recvWindow=6000)
    return len(response)

def getPNL(symbol, start, end):
    try:
        response = um_futures_client.get_account_trades(symbol=symbol, recvWindow=6000)
        for i in range(start,end): 
            realizedPnl = response[i]["realizedPnl"]
            commission = response[i]["commission"]
            pnl = float(realizedPnl) - float(commission)
            globalVar.pnl = globalVar.pnl + pnl
        
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )