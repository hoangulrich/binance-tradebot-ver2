import variables.globalVar as globalVar

def ask_input(symbol):
  symbol = str(symbol).upper()
  
  globalVar.x = 0
  globalVar.cumulativeMargin = 0
  globalVar.decimalPrecision = 5
  
  if symbol == None:
    # globalVar.symbol = "BLZUSDT"
    # globalVar.leverage = 20
    # globalVar.Xmax = 5
    # globalVar.gap = 0.2/100
    # globalVar.profit = 30/100
    # globalVar.quantity = 50
    # globalVar.power = 2
    # globalVar.BE = 5/100

    # globalVar.symbol = "OPUSDT"
    # globalVar.leverage = 20
    # globalVar.Xmax = 8
    # globalVar.gap = 0.5/100
    # globalVar.profit = 100/100
    # globalVar.quantity = 2
    # globalVar.power = 1.5
    # globalVar.BE = 5/100
    
    # globalVar.symbol = "MINAUSDT"
    # globalVar.leverage = 20
    # globalVar.Xmax = 8
    # globalVar.gap = 0.5/100
    # globalVar.profit = 100/100
    # globalVar.quantity = 6.5
    # globalVar.power = 1.5
    # globalVar.BE = 5/100
    
    globalVar.symbol = "BNXUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 8
    globalVar.gap = 0.5/100
    globalVar.profit = 100/100
    globalVar.quantity = 3.5
    globalVar.power = 1.5
    globalVar.BE = 5/100

  elif "BNX" in symbol:
    globalVar.symbol = "BNXUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 6
    globalVar.gap = 0.5/100
    globalVar.profit = 50/100
    globalVar.quantity = 4
    globalVar.power = 1.5
    globalVar.BE = 5/100

  elif "MINA" in symbol:
    globalVar.symbol = "MINAUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 6
    globalVar.gap = 0.5/100
    globalVar.profit = 50/100
    globalVar.quantity = 6.5
    globalVar.power = 1.5
    globalVar.BE = 5/100

  elif "OP" in symbol:
    globalVar.symbol = "OPUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 6
    globalVar.gap = 0.5/100
    globalVar.profit = 50/100
    globalVar.quantity = 2
    globalVar.power = 1.5
    globalVar.BE = 5/100

  elif "BLZ" in symbol:
    globalVar.symbol = "BLZUSDT"
    globalVar.leverage = 20
    globalVar.Xmax = 6
    globalVar.gap = 0.5/100
    globalVar.profit = 50/100
    globalVar.quantity = 50
    globalVar.power = 1.5
    globalVar.BE = 5/100
