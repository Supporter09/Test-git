
import datetime
import os
os.system("python card.py")

class normalCard:
    # def __init__(self):
    #     self.userId = ""
    #     self.userName = ""
    #     self.lastDate = x = datetime.datetime.now()
    #     self.allMoney = ""

    def __init__(self, userId, userName, lastDate,allMoney):
        self.__userId = userId
        self.__userName = userName
        self.__lastDate = lastDate
        self.__allMoney = allMoney

    def addMoney(self, money):
        self.__allMoney += money
        return self.__allMoney
    
    def getUserAllMoney(self):
        return self.__allMoney
    
    def printAllBasicCardData(self):
        cardDetail = [self.__userId,self.__userName,self.__lastDate,self.__allMoney]
        return cardDetail

    def setLastDate(self,newLastDate):
        self.__lastDate = newLastDate


    def getUserMoneyDetail(self):
        return self.__allMoney
