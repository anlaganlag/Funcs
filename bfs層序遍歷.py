# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, n: TreeNode) -> List[int]:
        if not n:
            return []
        q = collections.deque([n])
        ans = []
        while q:
            cur=q.popleft()
            ans.append( cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return ans

