from card import card

class VipCard:
    # Gọi tới constructor của lớp cha (card) 
     def __init__(self, __userId, __userName, __lastDate, __allMoney):
                
                # để gán giá trị vào thuộc tính của lớp cha.
        super().__init__(__userId, __userName, __lastDate, __allMoney)
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