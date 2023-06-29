import variables.globalVar as globalVar
from components.loopOrder import *
from components.endOrder import *
from components.restart import restart_stream
from module.positionIsEmpty import positionIsEmpty
from utils.printColor import *
from binanceAPI.teleBot import *


def algorithm(symbol, price, quantity, positionSide, type):

    # RESTART PROGRAM WHEN THERE ARE NO POSITION LEFT
    if positionIsEmpty(globalVar.symbol) == True:
        restart_stream()

    # MAIN ALGORITHM
    else:
        # ASSIGN INITIAL CEILING/FLOOR
        if globalVar.x == 0:
            # LONG 1ST
            # globalVar.initialCeiling = round(float(filledPrice),globalVar.decimalPrecision)
            # globalVar.initialFloor = round(globalVar.initialCeiling - globalVar.gap * globalVar.initialCeiling,globalVar.decimalPrecision)

            # SHORT 1ST
            globalVar.initialFloor = round(
                float(price), globalVar.decimalPrecision)
            globalVar.initialCeiling = round(
                globalVar.initialFloor + globalVar.gap * globalVar.initialFloor, globalVar.decimalPrecision)
            
            # LOG/INFO
            sendData("\n*******START*******" + f"\n{symbol}" +
                        "\n - Current Ceiling Price is: " + str(round(globalVar.initialCeiling, 4)) +
                        "\n - Current Floor Price is: " + str(round(globalVar.initialFloor, 4)) +
                        "\n https://www.binance.com/en/futures/"+globalVar.symbol)
            print("\nCeiling Price: " + str(round(globalVar.initialCeiling, 4)) +
                  "\nFloor Price: " + str(round(globalVar.initialFloor, 4))
                  +"\nChart:")
            print(f"\thttps://www.binance.com/en/futures/{globalVar.symbol}")

        # CALCULATE MARGIN/NAV
        globalVar.margin = round(float(globalVar.quantity) / globalVar.leverage *
                                 float(globalVar.initialCeiling), globalVar.decimalPrecision)
        globalVar.cumulativeMargin += globalVar.margin

        # LOG/INFO
        sendData(str(symbol) + " Order no. " + str(globalVar.x) +
                    "\n - Order is " + str(type) + " " + str(positionSide) +
                    "\n - Order margin is " + str(round(globalVar.margin, 2)) + " USDT" +
                    "\n - Total NAV is " + str(round(globalVar.cumulativeMargin, 2)) + " USDT")
        print("\nPHASE " + str(globalVar.x))

        # EVENT LOOP
        if globalVar.x < globalVar.Xmax:
            
            globalVar.x += 1
            globalVar.quantity = globalVar.quantity * globalVar.power

            if positionSide == "LONG":
                loopLong(globalVar.quantity)
            elif positionSide == "SHORT":
                loopShort(globalVar.quantity)

        # LAST ORDER/BREAK EVEN
        elif globalVar.x == globalVar.Xmax:
            globalVar.x += 1
            # if globalVar.x == globalVar.Xmax + 1:
            if positionSide == "LONG":
                endLong()
            else:
                endShort()
            # if globalVar.x == globalVar.Xmax + 2:
            #     if positionSide == "LONG":
            #         endFinalLong()
            #     else:
            #         endFinalShort()