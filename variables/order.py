import variables.globalVar as globalVar

class order:
    def __init__(self, symbol, id, type, price, quantity, status, side, positionSide):
        self.id = id
        self.type = type
        self.price = price
        self.quantity = quantity
        self.positionSide = positionSide
        self.status = status
        self.side = side
        self.symbol = symbol

    
    
    