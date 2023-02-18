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

def on_open(ws):
    exchange_info =  um_futures_client.exchange_info()
    for symbol in exchange_info["symbols"]:
        if symbol["symbol"] == globalVar.symbol:
            globalVar.decimalPrecision = symbol["pricePrecision"]
            globalVar.quantityPrecision = symbol["quantityPrecision"]
    initialOrder(globalVar.symbol)
    
def on_message(ws, message):
    #prYellow(f"\nMessage: {message}\n")
    event_dict = json.loads(message)
    #prYellow(json.dumps(event_dict, indent = 4))
    
    if event_dict["e"] == "ORDER_TRADE_UPDATE":

        # ASSIGN VARIABLE FOR ORDER
        price = event_dict["o"]["L"]
        quantity = event_dict["o"]["l"]
        positionSide = event_dict["o"]["ps"] #LONG/SHORT
        status = event_dict["o"]["X"] #NEW/EXPIRED/FILLED/CANCELED
        type = event_dict["o"]["o"] #STOP_MARKET/TAKE_PROFIT_MARKET
        id = event_dict["o"]["i"]
        side = event_dict["o"]["S"] #SELL/BUY
        symbol = event_dict["o"]["s"] #BTCUSDT

        if event_dict["o"]["X"] == "FILLED" and symbol == globalVar.symbol:
            # LOG
            prGreen(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")
            
            # START ALGORITHM 
            #if globalVar.expiredOrder == False:
            if id not in globalVar.orderList:
                algorithm(symbol, price, quantity, positionSide, type)
            
            
        elif event_dict["o"]["X"] == "EXPIRED" and symbol == globalVar.symbol:
            # LOG
            prRed(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")

            # FIX EXPIRED ORDER
            # limit = globalVar.Xmax - 1
            # globalVar.expiredOrder = True #test
            #algorithm(price, quantity, positionSide, type)
            
            # if getOrderCount(globalVar.symbol) == 2: #and globalVar.x < globalVar.Xmax:
            #     algorithm(price, quantity, positionSide, type)
            #     globalVar.expiredOrder = False #test
            # else:
            #     print("NO NEED FIX AT NUMBER OF ORDERS = " + str(getOrderCount(globalVar.symbol)))

            globalVar.orderList.append(id)
            if type != "TAKE_PROFIT_MARKET":
                algorithm(symbol, price, quantity, positionSide, type)
            # if getOrderCount(globalVar.symbol) == 2: #and globalVar.x < globalVar.Xmax:
            #     fixExpired(id,positionSide)
            # else:
            #     print("NO NEED FIX AT NUMBER OF ORDERS = " + str(getOrderCount(globalVar.symbol)))
        
        elif event_dict["o"]["X"] == "NEW" and symbol == globalVar.symbol:
            # LOG
            prYellow(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")
            #globalVar.orderList.append(id, type)
            
        elif event_dict["o"]["X"] == "PARTIALLY_FILLED" and symbol == globalVar.symbol:
            prRed(f"{symbol} | ID: {id} | Status: {status} | Side: {positionSide}-{side} | Type: {type}")
        
            
def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    sendData("\n*******END*******")
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    
    wsthread = threading.Thread(target = ws.run_forever, daemon = True)
    wsthread.start()
    
    while True:
        time.sleep(900)
        keepAlive()