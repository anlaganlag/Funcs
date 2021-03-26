

import random
#各个牌型的权重
weight = {"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"11":9,"12":10,\
          "13":11,"1":12,"2":13,"14":14,"15":15}
#各个牌型显示效果
show = {"1":"A","10":"0","11":"J","12":"Q","13":"K","14":"X2","15":"X1"}
#花色
cardType = ["S","H","C","D"]

#一副完整的新牌型
def makeDeck():
    deck = []
    cardNum=52
    for i in range(cardNum):
    #牌的点数即4个一组,点数加上花色
        deck.append(str(i//4+1)+" " +cardType[i%4])
    #加上大小王14小王即X2,15大王即X1
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
        ans.append(sorted(deck[i:i+gap],key=lambda x:-weight[x.split(" ")[0]]))
    h1,h2,h3,remain = ans
    return h1,h2,h3,remain



def showIt(l):
    ans = []
    for i in l:
        if i in ["14","15"]:
            ans.append(show[i])
        else:
            cardPoint,cardType= i.split(" ")
            if show.get(cardPoint):
                ans.append(show[cardPoint]+cardType)
            else:
                ans.append(cardPoint+cardType)
    return ans
            
a1,a2,a3,r = makeShuffleDeck()
print([showIt(a1),showIt(a2),showIt(a3),showIt(r)])

