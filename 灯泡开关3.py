"""
遍历lightss持续更新关注序号最大的灯:

在遍历时:
如果遇到灯的index小于last的号码,则证明last前面还有空位.

如果遇到的灯的index大于last的号码,则更新本灯为新的last
python
        last= max(last,cur)# 用last记录最后的灯
如果最后的last的号码和当前遇到灯的index一致的时,证明last及last前的灯都是亮的
python
        ans +=1
代码
"""
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
#一句话理解就是last就是开坑,index追上last的过程就是填坑的过程
#如果index追上了last,那么就是坑已经填满
        n = len(light)
        last = ans =0
        for i,cur in enumerate(light,1):
            last= max(last,cur)
#这个记录最大值的常用套路
            if i == last:
                ans +=1
        return ans

#简单来理解就是..last决定要填充的坑有多大
#index决定已经填充的材料有多少
#假设坑和材料相等,即已经填充完毕..
   #如果每次坑增加1,且材料增加1则满足的情况+1
   #否则又得坑和材料相等才能满足情况一次

def open_light(light):
    """
    思路是考慮當前位置前後的情況:
        前後都0,則相當於挖坑即cnt+1
        前0後1,縮小坑cnt-1但是,坑沒有完全填上
        前後都1,cnt變成0,即坑已經被
    總之就是前面0就是坑+1,前面是1沒有開新坑
          後面是1就是坑-1,後面0沒有變化

    簡單來說就是1 1 的情況-1
              0 0      +1
              1 0  不變
              0 1   +1-1
    """
          
    cur = [1]+(len(light)+1)*[0]
    cnt =0
    ans =0
    for i in light:
        cnt +=not cur[i-1]
        cnt -= cur[i+1]
        cur[i]  = 1
        if cnt == 0:
            ans +=1
    return ans
        
l3=[4,1,2,3]
print(openlight(l3))
"""
房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。

在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。

灯的颜色要想 变成蓝色 就必须同时满足下面两个条件：

灯处于打开状态。
排在它之前（左侧）的所有灯也都处于打开状态。
请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目 。
"""
