from nhadat import trading

class houseTrading(trading):
    def init(self, tradingCode, tradingDay,price, typeOfHouse, square,houseIndex):
        self.trading_code = str(trading_code)
        self.trading_day = trading_day
        self.price = price
        self.type = str(type_of_house)
        self.square = square
        self.house_index = house_index


    def getPriceWithoutVAT(self):
        if self.type ==0:
            paid =self.price = self.square * self.price * self.houseIndex
            return paid
        paid = self.price = self.square * self.price * self.houseIndex *1.5
        return paid

    def getPriceWithVAT(self):
        if self.type == 0:
            paid = self.square * self.price * self.houseIndex +( self.square * self.price * self.houseIndex )*0.05
            return paid
        paid = self.square * self.price * self.houseIndex *1.5 + (self.square * self.price * self.houseIndex *1.5)*0.05
        return paid

    def setData(self):
        trading_day = str(input("type your trading day here (ex: 11/10/2020): "))
        price = input("Type the price: ")
        type_of_house = input("Type your type of trade btw cao cap(0) va biet thu(1):")
        square = input("Type square: ")
        house_index = input("Type house index")
        self.trading_code = str(trading_code)
        self.trading_day = trading_day
        self.price = price
        self.type = str(type_of_house)
        self.square = square
        self.house_index = house_index
