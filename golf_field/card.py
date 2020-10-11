from abc import ABC, abstractclassmethod
# from Date import Date
import os
os.system("python Date.py")
class card(ABC):

    @abstractclassmethod
    def addMoney(self):
        pass
    
    def removeAllMoney(self):
        pass


class normalCard(card):
    def __init__(self, userId, userName, lastDate,allMoney):
        self.__userId = userId
        self.__userName = userName
        self.__firstDate = Date(1,2,2020)
        self.__lastDate = lastDate
        self.__allMoney = allMoney

    def addMoney(self, money):
        self.__allMoney += money
        return self.__allMoney
    
    def removeAllMoney(self):
        if getDifference(self.__firstDate, self.__lastDate) > 365:
            self.__allMoney = 0

    def getUserAllMoney(self):
        return self.__allMoney
    
    def printAllBasicCardData(self):
        cardDetail = [self.__userId,self.__userName,self.__lastDate,self.__allMoney]
        return cardDetail

    def setLastDate(self,newLastDate):
        self.__lastDate = newLastDate


    def getUserMoneyDetail(self):
        return self.__allMoney

    

class VipCard(card):
    # Gọi tới constructor của lớp cha (card) 
     def __init__(self, userId, userName, lastDate, allMoney):
        self.__userId = userId
        self.__userName = userName
        self.__firstDate = Date(1,2,2020)
        self.__lastDate = lastDate
        self.__allMoney = allMoney
        self.__yearOfVip = 0
        self.__bonusPercentMoney = 0

        def printAllBasicCardData(self):
            cardDetail = [self.__userId,self.__userName,self.__lastDate,self.__allMoney,self.__yearOfVip]
            return cardDetail

        def bonusPercentMoneyVip(self):
            self.__bonusPercentMoney = max(self.yearOfVip * 0.02,0.2)
            return self.__bonusPercentMoney

        def addMoney(self,money):
            self.__allMoney += money + money*self.__bonusPercentMoney
            return self.__allMoney

        def removeAllMoney(self):
            if getDifference(self.__firstDate, self.__lastDate) > 365:
                self.__allMoney = 0

