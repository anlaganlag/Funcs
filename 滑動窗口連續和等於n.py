
def findContinuousSequence(target):
"""簡單來說就是連續的和等於target,從小到大返回所有滿足的連續和
   用的是樸素滑動窗口
   如果擴大窗口就是+j且j的index+1
   如果縮小窗口就是-i且i的index+1
   總之i和j都不需要回溯.O(n)
   且要注意左包右不包..左閉右開
   


"""
    i,j,sum_,ans=1,2,1,[]
    while i <= target//2:
        if sum_<target:
            sum_+=j
            j+=1
            #有j的index本來就是開的所以直接+j,再更新index+1
        elif sum_> target:
            sum_ -= i
            i+=1
        else:
            ans.append(list(range(i,j)))
            #由於符合左閉右開,直接range即可
            sum_ -= i
            i+=1
    return ans

"""
输入
9
输出
[[2,3,4],[4,5]]
"""
