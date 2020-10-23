from Date import Date
from card import Card

class VipCard(Card):
    # Gọi tới constructor của lớp cha (card) 
    def __init__(self, user_id, user_name, last_date, all_money):
        self.user_id = user_id
        self.user_name = user_name
        self.first_date = Date(1,2,2020)
        self.last_date = last_date
        self.all_money = all_money
        self.year_of_vip = 0
        self.bonus_percent_money = 0

    def addMoney(self,money):
        self.all_money = money + money*self.bonus_percent_money
        return self.all_money

    def printAllBasicCardData(self):
        cardDetail = [self.user_id,self.user_name,self.last_date,self.all_money,self.year_of_vip]
        return cardDetail

    def bonusPercentMoneyVip(self):
        self.bonus_percent_money = max(self.year_of_vip * 0.02,0.2)
        return self.bonus_percent_money

    def removeAllMoney(self):
        if getDifference(self.first_date, self.last_date) > 365:
            self.all_money = 0

