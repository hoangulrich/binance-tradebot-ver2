import variables.globalVar as globalVar
import json

with open("input.json", "r") as read_file:
  data = json.load(read_file)

input = data["input"]

def ask_input(symbol):
  symbol = str(symbol).upper()
  
  globalVar.x = 0
  globalVar.cumulativeMargin = 0
  globalVar.decimalPrecision = 5
  
  # DEFAULT
  if symbol == None:
    globalVar.symbol = "BNXUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 8
    globalVar.gap = 0.5/100
    globalVar.profit = 100/100
    globalVar.quantity = 3.5
    globalVar.power = 1.5
    globalVar.BE = 5/100
  
  # WITH SPECIFIC SYMBOL 
  else:
    for i in input:
      if symbol in i["symbol"]:
        globalVar.symbol = i["symbol"]
        globalVar.leverage = i["leverage"]
        globalVar.Xmax = i["Xmax"]
        globalVar.gap = i["gap"]/100
        globalVar.profit = i["profit"]/100
        globalVar.quantity = i["quantity"]
        globalVar.power = i["power"]
        globalVar.BE = i["BE"]/100
    
    
