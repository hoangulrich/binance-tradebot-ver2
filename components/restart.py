import variables.globalVar as globalVar
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from utils.printColor import *
from datetime import datetime
from binanceAPI.teleBot import *
from components.startLoop import initialOrder
from input import *
import os

def restart_stream():
  # CLEAR LEFTOVER ORDERS
  cancelOrder(globalVar.symbol)
  prCyan("CANCEL ALL ORDERS(restart)")

  # CALCULATE PNL AND DURATION
  pnl = round(getBalance() - globalVar.initialBalance, 4)
  duration = getDuration()
  record(pnl, duration)

  # SEND INFO TELEGRAM + LOG
  sendData("PNL: " + "$" + str(pnl) + "\nGain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) +"%"
  + "\n*******RESTART*******")
  print("PNL: " + "$" + str(pnl) + " | GAIN: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) +"%")
  prCyan("\n*******RESTART*******")

  # RESTART (server)
  # globalVar.orderList.clear()
  ask_input()
  initialOrder(globalVar.symbol)

  # RESTART (local)
  # os.system('python "main.py"')
  

def getDuration():
  globalVar.end = datetime.now()
  duration = globalVar.end - globalVar.start
  duration = str(duration)[:-7]
  return duration


def record(pnl, duration):
  f = open("pnl.txt", "a")
  f.write("\n" + str(globalVar.symbol) + " " + str(round(getBalance(), 2)) +
          " " + str(pnl) + " " + str(round(pnl/globalVar.cumulativeMargin*100,2)) + "%" + " " + str(globalVar.x-1) + " " + str(duration) +
          " " + str(globalVar.start) + " " + str(globalVar.end))
  f.close()