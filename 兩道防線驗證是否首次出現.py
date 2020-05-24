


#思路比較有意思..
#只要沒有在v裏面都默認是首次出現..
#會添加到q隊列裏面...
#第二次出現有點牛逼..第二次出現首先通過了沒有visited..但是在q裏面顯示出現過..
#所以第二次出現是該算法的關鍵..第二次出現才會進入visited..並刪除在q中的存在..
#第三次及以後讀直接fail..

#用小劇場理解就是首次和第二次都是可以通過v..
#但是第二次不能通過q..
#會處罰v記錄和q刪除..
#所以是兩層防線一是v主要是對付第三次進入直接拒絕..
#q是第二次進入觸發v和q自淨化..
class Solution:
    def firstUniqChar(self, s: str) -> str:
        v = set()#v相當於visited,判斷是否訪問過
        q = []#存儲第一個出現的字母
        for i in s:
            if i not in v:#對於每個字母如果沒有出現過程才處理,出現過直接continue
                if i in q:#q默認是存儲只出現一次的字母,但是第二次出現需要添加到v已經訪問裏,刪除從q中刪除..
                    v.add(i)
                    del q[q.index(i)]
                else:
                    q.append(i)#首次出現加入q隊列
        return q[0] if q else ' '#唯一的結果取出第一個即可
