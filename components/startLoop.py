import variables.globalVar as globalVar
from module.newMarketOrder import *
from module.getBalance import *
from datetime import datetime
from module.newOrder import *
from utils.printColor import *
from module.cancelOrder import *

# CREATE NEW MARKET ORDER INITIALLY
def initialOrder(symbol):
  globalVar.initialBalance = getBalance()
  globalVar.start = datetime.now()
  
  prCyan("\nINITIAL ORDER(startloop)")
  # newMarketOrder(globalVar.symbol, "LONG", "BUY", "MARKET", globalVar.quantity)
  newMarketOrder(symbol, "SHORT", "SELL", "MARKET", globalVar.quantity)

