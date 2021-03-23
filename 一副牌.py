
"""
完整的一副牌
"""



import random
# map = {52:"w",53:"W", 10:"T",11:"J",12:"Q",13:"K",1:"A"}
map = {52:"小王",53:"大王",21:"A",22:"2",11:"J",12:"Q",13:\
       "K",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"T"}
def makeDeck():
    deck = []
    for i in range(54):
        cardPoint = i//4+1
        if i>=52:
            deck.append(i)
        elif i < 8:
          deck.append(cardPoint+20)  
        else:
            deck.append(cardPoint)
    return deck
        
def makeShuffleDeck():
    deck =makeDeck()
    random.shuffle(deck)
    a,b,c,d= [sorted(deck[:17]),sorted(deck[17:34]),sorted(deck[34:51]),sorted(deck[51:])]
    c1,c2,c3 = sorted(a+d),sorted(b+d),sorted(c+d),
    return a[::-1],b[::-1],c[::-1],d[::-1],c1[::-1],c2[::-1],c3[::-1]

def randomPick():
    lst = list(range(3,14))+[21,22]
    random.shuffle(lst)
    ans1=lst.pop()
    ans2=lst.pop()
    return ans1,ans2

def convertToChar(l):
    ans = ""
    for i in l:
        if i>=10 or i <2:
            if i == pick1:
                ans += f"({str(map[i])}) "
                continue
            elif i== pick2:
                ans += f"<{str(map[i])}> "
                continue
            ans += map[i]+" "

        else:
            if i == pick1:
                ans += f"({str(i)}) "
                continue
            elif i == pick2:
                ans += f"<{str(i)}> "
                continue
            ans += str(i)+" "
    return ans

def findBomb(l):
    pass


pick1,pick2=randomPick()
# print(f'发牌前赖子({map[pick1]}) \n发牌后赖子是<{map[pick2]}>')
h1,h2,h3,extras,c1,c2,c3 = makeShuffleDeck()
# print(convertToChar(extras))
# print(convertToChar(h1),convertToChar(c1))
# print(convertToChar(h2),convertToChar(c2))
# print(convertToChar(h3),convertToChar(c3))

print(convertToChar(c1).split(" "))
# print(convertToChar(c2))
# print(convertToChar(c3))





