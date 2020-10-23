from Date import Date
from card import Card

class VipCard(Card):
    # Gọi tới constructor của lớp cha (card) 
    def __init__(self, userID, userName, lastDate, allMoney):
        self.userID = userID
        self.userName = userName
        self.firstDate = Date(1,2,2020)
        self.lastDate = lastDate
        self.allMoney = allMoney
        self.yearOfVip = 0
        self.bonusPercentMoney = 0

    def addMoney(self,money):
        self.allMoney = money + money*self.bonusPercentMoney
        return self.allMoney

    def printAllBasicCardData(self):
        cardDetail = [self.userID,self.userName,self.lastDate,self.allMoney,self.yearOfVip]
        return cardDetail

    def bonusPercentMoneyVip(self):
        self.bonusPercentMoney = max(self.yearOfVip * 0.02,0.2)
        return self.bonusPercentMoney

    def removeAllMoney(self):
        if getDifference(self.firstDate, self.lastDate) > 365:
            self.allMoney = 0

