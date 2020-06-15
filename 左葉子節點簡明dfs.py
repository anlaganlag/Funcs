
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#只分兩種情況1是有zuoyezi節點,和沒有zuoyezi節點..
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def h(n):
            if not n:
                return 0
            if n.left and n.left.left == None and n.left.right == None:
                return n.left.val + h(n.right)#有左葉子節點的情況
            return h(n.left)+h(n.right)#不含左葉子節點的情況..
        return h(root)
        
