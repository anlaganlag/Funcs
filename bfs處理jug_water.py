from collections import defaultdict
def bfs(a1,a2,aim):
    map = defaultdict(lambda:False)
    path = []
    q = [(0,0)]

    while q:
        curr = q.pop()
        isSolvable = False
        if map[curr] == True:
            continue
        if curr[0] > a1 or curr[1] > a2 or curr[0] < 0 or curr[1] <0 :
            continue
        if map[(curr[0],curr[1])] == False:
            path.append((curr[0],curr[1]))
            map[(curr[0],curr[1])]  = True
        
        if curr[0] == aim or curr[1] ==aim:
            isSolvable = True
            if curr[0] == aim:
                if curr[1] != 0:
                    path.append((curr[0],0))
            else:
                if curr[0] != 0:
                    path.append((0,curr[1]))
            sz = len(path)
            for  i in range(sz):
                print(path[i])
            break
        if map[(curr[0],a2)] == False:
            q.append((curr[0],a2))
           
            
        if map[(a1,curr[1])] == False:
            q.append((a1,curr[1]))
          
        
        for ap in range(1,max(a1,a2)+1):
            c = curr[0]+ap
            d = curr[1]-ap
            if (c == a1 and d >=0) or ( c<= a1 and d ==0):
                if map[(c,d)] == False:
                    q.append((c,d))
                  
            c = curr[0] -ap
            d = curr[1] +ap
            if (d == a2 and c >= 0) or ( d <= a2 and c ==0):
                if map[(c,d)] == False:
                    q.append((c,d))
                    
        if map[(curr[0],0)] ==False:
            q.append((curr[0],0))
            
        if map[(0,curr[1])] ==False:
            q.append((0,curr[1]))
            
    if not isSolvable:
        print("無解")
j1,j2,aim =157,223,72
print("Steps")
bfs(j1,j2,aim)


"""
#稍微優化了下代碼DRY
  且加上了注釋

輸出結果有些小問題需要再理順一邊
  
from collections import defaultdict
def bfs(a1,a2,aim):
    #a1和a2是其實是j1和j2的罐子 ,嘗試湊出aim的目標
    map = defaultdict(lambda:False)
    #defaultdict主要用來記錄是否已經嘗試過,如果是嘗試過的會跳出while循環
    path = []
    #path會記錄所有第一出現的路進其實就是配合map使用的
    q = [(0,0)]
    #q就是工具變量,就是存儲bfs的典型隊列函數
    while q:
        #只要還能嘗試,就會while裏面的flag函數默認是設置爲False,但是如果達到了aim,會將flag切換成True
        curr = q.pop(0)#bfs隊列的第一位彈出,用於處理
        isSolvable = False
        if map[curr] == True:#如果處理過了,繼續
            continue
        if curr[0] > a1 or curr[1] > a2 or curr[0] < 0 or curr[1] <0 :
            continue
        if map[(curr[0],curr[1])] == False:
            path.append((curr[0],curr[1]))
            map[(curr[0],curr[1])]  = True
        
        if curr[0] == aim or curr[1] ==aim:
            isSolvable = True
            if curr[0] == aim:
                if curr[1] != 0:
                    path.append((curr[0],0))
            else:
                if curr[0] != 0:
                    path.append((0,curr[1]))
            sz = len(path)
            for  i in range(sz):
                print(path[i])
            break#打印出結果後,直接就退出了while循環
        q.append((curr[0],a2))
        q.append((a1,curr[1]))
        q.append((curr[0],0))
        q.append((0,curr[1]))
        for ap in range(1,max(a1,a2)+1):
            c = curr[0]+ap
            d = curr[1]-ap
            if (c == a1 and d >=0) or ( c<= a1 and d ==0):
                    q.append((c,d))
            c = curr[0] -ap
            d = curr[1] +ap
            if (d == a2 and c >= 0) or ( d <= a2 and c ==0):
                    q.append((c,d))
    if not isSolvable:
        print("無解")
j1,j2,aim =157,223,72
#j1,j2,aim =4,3,2
print("Steps:")
bfs(j1,j2,aim)









from collections import defaultdict
def bfs(a1,a2,aim):
    #a1和a2是其實是j1和j2的罐子 ,嘗試湊出aim的目標
    map = defaultdict(lambda:False)
    #defaultdict主要用來記錄是否已經嘗試過,如果是嘗試過的會跳出while循環
    path = []
    #path會記錄所有第一出現的路進其實就是配合map使用的
    q = [(0,0)]
    #q就是工具變量,就是存儲bfs的典型隊列函數
    while q:
        #只要還能嘗試,就會while裏面的flag函數默認是設置爲False,但是如果達到了aim,會將flag切換成True
        curr = q.pop(0)#bfs隊列的第一位彈出,用於處理
        isSolvable = False
        if map[curr] == True:#如果處理過了,繼續
            continue
        if curr[0] > a1 or curr[1] > a2 or curr[0] < 0 or curr[1] <0 :
            continue
        path.append(curr)
        map[curr]  = True
        
        if curr[0] == aim or curr[1] ==aim:
            isSolvable = True
            if curr[0] == aim:
                if curr[1] != 0:
                    path.append((curr[0],0))
            else:
                if curr[0] != 0:
                    path.append((0,curr[1]))
            sz = len(path)
            for  i in range(sz):
                print(path[i])
            break#打印出結果後,直接就退出了while循環
        q.append((curr[0],a2))
        q.append((a1,curr[1]))
        
        for ap in range(1,max(a1,a2)+1):
            c = curr[0]+ap
            d = curr[1]-ap
            if (c == a1 and d >=0) or ( c<= a1 and d ==0):
                q.append((c,d))
            c = curr[0] -ap
            d = curr[1] +ap
            if (d == a2 and c >= 0) or ( d <= a2 and c ==0):
                q.append((c,d))
        q.append((curr[0],0))
        q.append((0,curr[1]))
    if not isSolvable:
        print("無解")
# j1,j2,aim =157,223,72
j1,j2,aim =224,233,168
print("Steps:")
bfs(j1,j2,aim)


"""
