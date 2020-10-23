from abc import ABC, abstractclassmethod
# from Date import Date
from Date import Date

class Card(ABC):

    @abstractclassmethod
    def addMoney(self):
        pass
    
    def removeAllMoney(self):
        pass

