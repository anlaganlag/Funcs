class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        l = {}
	#存储首先出现在左边的节点
        ans = 0
        def h(n,w=0,d=0):
            nonlocal l,ans
            if  n:
                l.setdefault(d,w)
                ans = max(ans,w-l[d]+1)
                h(n.left,2*w,d+1)
                h(n.right,2*w+1,d+1)
        h(root)
        return ans
"""
662. 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。


"""

