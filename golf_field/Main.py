from NormalCard import NormalCard
from VipCard import VipCard
from Date import Date

def main():
    moi = NormalCard(1001,"huy",Date(1,2,2020),200)
    print(moi.printAllBasicCardData())
    moi_2 = VipCard(1001,"huy",Date(1,2,2020),200)
    print(moi_2.printAllBasicCardData())

if __name__ == "__main__":
    main()