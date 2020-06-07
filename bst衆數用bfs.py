# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dic = collections.defaultdict(int)
        q = [root]
        while q:
            n = q.pop()
            dic[n.val]+=1
            if n.right:
                q.append(n.right)
            if n.left:
                q.append(n.left)
        res = []
        mex_ele = max(dic.values())
        for k,v in dic.items():
            if v ==mex_ele:
                res.append(k)
        return res
