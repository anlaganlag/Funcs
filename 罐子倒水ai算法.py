from collections import defaultdict
#defaultdict真的牛逼
j1,j2,aim = 4,3,2
#j1,j2相當於罐子的最大容量,aim是目標容量
visited = defaultdict(lambda:False)
#初始化的defaultdict,且默認值爲false
def w(a1,a2):
#該遞歸函數會打印中間步驟
	且會通過的True或者False表明是否可解
#且a1和a2是當前的水含量
    if (a1==aim and a2==0)  or (a1==0 and a2 == aim):
#用if語句檢查是否已經達到的目標,也就是base情況
        print((a1,a2))
        return True
    if visited[(a1,a2)] == False:
#檢查是否是新的組合情況,如果是新的組合即這裏值會是false
#簡單來說就是若該組合是False,就是這是新情況
        print((a1,a2))
#由於滿足是新情況,此時需要打印 
        visited[(a1,a2)] =True
#修改flag爲True,也就是說明這個現在不是新情況
#簡單來說就是True都是出現過的情況,且該種情況會存儲到字典裏面defaultdict
#True 等於已經訪問
        return w(0,a2) or\ # 要麼是清空j1,將就j1倒空
               w(a1,0) or\ #           j2     j2
               w(j1,a2) or\#       補充滿j1
               w(a1,j2) or\#             j2
               w(a1+min((j1-a1),a2),a2-min((j1-a1),a2)) or \
                           # j1填滿(如果a2>需填滿),j2清空( a2<需填滿)
               w(a1-min((j2-a2),a1),a2+min((j2-a2),a1))
                          #   j2        a1         j1      a2
#遞歸地推進6種可能的子情況,持續下去嘗試達到目標
    else:

#假如一直達不到base情況,會返回false,無解
        return False


print(w(0,0))
    

collections 的defaultdict


