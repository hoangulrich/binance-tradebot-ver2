import websocket, json, threading, time
from utils.printColor import *
from algorithm import *
from binanceAPI.datastream import *
from binanceAPI.teleBot import *
from module.newMarketOrder import *
from components.startLoop import initialOrder
from variables import globalVar
from components.fixOrder import *
from module.getOrderCount import *
from module.getPosition import *

def on_open(ws):
    # GET EXCHANGE INFO AND START INITIAL ORDER
    exchange_info =  um_futures_client.exchange_info()
    for symbol in exchange_info["symbols"]:
        if symbol["symbol"] == globalVar.symbol:
            globalVar.decimalPrecision = symbol["pricePrecision"]
            globalVar.quantityPrecision = symbol["quantityPrecision"]
    initialOrder(globalVar.symbol)
    
def on_message(ws, message):
    event_dict = json.loads(message)
    #prYellow(json.dumps(event_dict, indent = 4))
    
    if event_dict["e"] == "ORDER_TRADE_UPDATE" and event_dict["o"]["s"] == globalVar.symbol:

        # ASSIGN VARIABLE FOR ORDER
        price = event_dict["o"]["L"]
        quantity = event_dict["o"]["l"]
        positionSide = event_dict["o"]["ps"] #LONG/SHORT
        status = event_dict["o"]["X"] #NEW/EXPIRED/FILLED/CANCELED
        type = event_dict["o"]["o"] #STOP_MARKET/TAKE_PROFIT_MARKET
        id = event_dict["o"]["i"]
        side = event_dict["o"]["S"] #SELL/BUY
        symbol = event_dict["o"]["s"] #BTCUSDT

        if status == "FILLED":
            # LOG
            prGreen(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")
            
            # START ALGORITHM 
            globalVar.filledOrderList.append(id)
            if id not in globalVar.expiredOrderList:
                algorithm(symbol, price, quantity, positionSide, type)
            
        elif status == "EXPIRED":
            # LOG
            prRed(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")

            # FIX EXPIRED ORDER
            globalVar.expiredOrderList.append(id)
            if (type != "TAKE_PROFIT_MARKET") or (type == "TAKE_PROFIT_MARKET" and positionIsEmpty(globalVar.symbol) == True):
                algorithm(symbol, price, quantity, positionSide, type)
        
        elif status == "NEW":
            # LOG
            prYellow(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")
            
            # FIX FILLED ORDER DOESNT SHOW
            if getOrderCount(symbol) == 0 and globalVar.x == 0 and id not in globalVar.expiredOrderList:
                globalVar.expiredOrderList.append(id)
                algorithm(symbol, getPositionPrice(symbol, "SHORT"), quantity, positionSide, type)
            
        elif status == "PARTIALLY_FILLED":
            prGreen(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")

        else:
            prCyan(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")

            
def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    
    wsthread = threading.Thread(target = ws.run_forever, daemon = True)
    wsthread.start()
    
    while True:
        time.sleep(900)
        keepAlive()