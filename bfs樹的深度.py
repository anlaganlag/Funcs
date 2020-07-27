# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_level=1
        from collections import deque
        q = deque([(root,1)])#注意裏面是列表放入tuple..
        while q:
            cur,level = q.popleft()
            max_level=max(max_level,level)
            if cur.left:
                q.append([cur.left,level+1])
            if cur.right:
                q.append([cur.right,level+1])
        return max_level
            

