# import golf_field_vip
import datetime

class card:
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

    

huy_tran = card("0101","huy_tran","11/9",1000)

print(huy_tran.addMoney(1000))
print(huy_tran.printAllBasicCardData())

card_detail = huy_tran.printAllBasicCardData()
class cardVIP(card):
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

if huy_tran.getUserAllMoney() >500:
    cardVipDetail = cardVIP(card_detail[0],card_detail[1],card_detail[2],card_detail[3])

print(cardVipDetail.printAllBasicCardData())
print(cardVipDetail.addMoney(1000))