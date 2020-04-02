class Solution:
    def verifyPostorder(self, n: List[int]) -> bool:
        def h(i,j):
            if i >= j: # i =j 即只有一个元素,比如为真,符合bst
                return True           #如果i>j即0个元素,也满足bst
            p = i  #p是从头到尾遍历的指针
            while n[p] <n[j]:
                p+=1
            mid = p
            while n[p] >n[j]:
                p+=1
            return p == j and h(i,mid-1) and h(mid,j-1)

        return h(0,len(n)-1)


#首先是基线条件牛逼..
#其次两个while将p指针从头到尾巴一直传递真的是牛逼到不行..
#即将数组按照n[j] 最后一位分成了两端,前面那段是比n[j] 小的 后面那段是比n[j]大的 如果p由此传递到底部,说明改数满足bst的性质
#即 left < root < right
#且根据获得mid即第一个比root大的数..
#两部分依次在递归的的調用,如一mid-1就是小於n[j]的邊界條件
#而mid就是比n[j]大的首個值所以需要包括,但是最後一個由於是root所以要排除..
#真的精妙無比
#













