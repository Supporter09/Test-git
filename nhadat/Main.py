from houseTrading import houseTrading
from realEstate import realEstate


TradingCodeList = []
def WriteDateIntoList(typeOfTrading):
    tradingList =[]
    if typeOfTrading. == 0:
        tradingCode = str(input("type your trading code here: "))
        while tradingCode!="":
            trade = realEstate(tradingCode,tradingDay,price,typeOfTrade,square)
            tradingList.append(trade)
    elif typeOfTrading==1:
        tradingCode = str(input("type your trading code here: "))
        while tradingCode!="" :
            trade = houseTrading(tradingCode,tradingDay,price,typeOfTrade,square)
            tradingList.append(trade)


userTypeOfTrade = input("choose your type of trade btw realestate(0) and housetrading(1): ")
WriteDateIntoList(userTypeOfTrade)