from Date import Date
from card import Card

class NormalCard(Card):
    def __init__(self, userId, userName, lastDate,allMoney):
        self.userId = userId
        self.userName = userName
        self.firstDate = Date(1,2,2020)
        self.lastDate = lastDate
        self.allMoney = allMoney

    def addMoney(self, money):
        self.allMoney += money
        return self.allMoney
    
    def removeAllMoney(self):
        if getDifference(self.firstDate, self.last_date) > 365:
            self.allMoney = 0

    def getUserAllMoney(self):
        return self.allMoney
    
    def printAllBasicCardData(self):
        cardDetail = [self.userId,self.userName,self.lastDate,self.allMoney]
        return cardDetail

    def setLastDate(self,newLastDate):
        self.lastDate = newLastDate


    def getUserMoneyDetail(self):
        return self.allMoney
