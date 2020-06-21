
"""
124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def h(n):
            nonlocal ans
            if n == None:
                return 0
            l,r = max(h(n.left),0),max(h(n.right),0)
            ans = max(ans,l+r+n.val)
            return max(l,r)+n.val#返回是l或者r最大值..
        ans = float("-inf")
        h(root)
        return ans
