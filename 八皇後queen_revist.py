class Solution:
    def totalNQueens(self, m: int) -> int:
        def check(y,x,chess):#判斷當前位置對上左上和右上的殺傷..殺傷到返回0,沒有殺傷可以放置就是1
            for row in range(y):#考慮當前放置的y,x會不會對上面的放置的queen進行殺傷..
                if(chess[row][x] == 1):#對上方的每個格子進行一次殺傷..
                    return 0                     
                if(x-1-row >=0):#其實就是測試col左邊那格是否存在,存在就檢查左斜上方
                    if (chess[y-1-row][x-1-row] == 1):
                        return 0
                if(x+1+row<m):#同理就是檢查col右邊那格是否存在,存在就檢查右邊斜上方
                    if(chess[y-1-row][x+1+row] == 1):
                        return 0
            return 1
        def lay_queens(y,chess):#按照每行放置queens
            nonlocal ans,m
            if y == m:#如果到達了不存在的那格,就是找到了一個解法.
                ans+=1
                return#正是這個return非常精髓,return就是return None,就好比之前的數獨問題
                #就是靠input()也是相當於一個return,return之後會進行下一個不走即歸零chess[y][x]=0
            for x in range(m):
                if check(y,x,chess):
                    chess[y][x] = 1
                    lay_queens(y+1,chess)
                    chess[y][x] = 0
        ans =0
        chess = [m*[0] for row in range(m)]
        lay_queens(0,chess)#從第0行開始放置
        return ans
