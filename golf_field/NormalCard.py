from Date import Date
from card import Card

class NormalCard(Card):
    def __init__(self, user_id, user_name, last_date,all_money):
        self.user_id = user_id
        self.user_name = user_name
        self.first_date = Date(1,2,2020)
        self.last_date = last_date
        self.all_money = all_money

    def addMoney(self, money):
        self.all_money += money
        return self.all_money
    
    def removeAllMoney(self):
        if getDifference(self.first_date, self.last_date) > 365:
            self.all_money = 0

    def getUserAllMoney(self):
        return self.all_money
    
    def printAllBasicCardData(self):
        cardDetail = [self.user_id,self.user_name,self.last_date,self.all_money]
        return cardDetail

    def setLastDate(self,newLastDate):
        self.last_date = new_last_date


    def getUserMoneyDetail(self):
        return self.all_money
