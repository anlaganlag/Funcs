class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        ans = []
        cnt=1
        while q:
            nq=[]
            l = []
            for n in q:
                if n:
                    l.append(n.val)
                    if cnt:
                        nq.extend([n.left,n.right])
                    else:
                        nq.extend([n.right,n.left])
            if l:
                ans.append(l)#這裏的值保證是在按正確信息開始正.下一層反..
#交替進行..
            q = nq[::-1]#相當於每層都反轉一次..
            cnt ^= 1#cnt這裏是flag標記指明現在是哪一層..0->1 1->1
        return ans

"""
面试题32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 
"""
