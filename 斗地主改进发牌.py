
import random
#各个牌型的权重
weight = {"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"11":9,"12":10,\
          "13":11,"1":12,"2":13,"14":14,"15":15}
#各个牌型显示效果
show = {"10":"T","11":"J","12":"Q","13":"K","1":"A","14":"小王","15":"大王"}



#一副完整的新牌型
def makeDeck():
    deck = []
    cardNum=52
    for i in range(cardNum):
    #牌的点数即4个一组
        deck.append(str(i//4+1))
    #加上大小王
    deck.extend(["14","15"])
    return deck

#洗牌操作
def makeShuffleDeck():
    ans = []
    deck =makeDeck()
    random.shuffle(deck)
    gap = 17
    total = 54
    for i in range(0,total,gap):
    #根据权重从大到小排序
        ans.append(sorted(deck[i:i+gap],key=lambda x:-weight[x]))
    h1,h2,h3,remain = ans
    return h1,h2,h3,remain
