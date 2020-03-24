from collections import defaultdict
class Solution:
    memo =defaultdict(int)
    def rob(self, root: TreeNode) -> int:
        def h(root,m):
            if not root:
                return 0
            if m[root]: 
                return m[root]
            tmp = root.val
            if root.left:
                tmp += h(root.left.left, m) + h(root.left.right, m)
            if root.right:
                tmp += h(root.right.left, m) + h(root.right.right,m)
            ans = max(tmp, h(root.left, m) + h(root.right, m))
            m[root] = ans
            return ans
        return h(root,self.memo)
#除了defaultdict之外,也可以用lru_cache
from functools import lru_cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def h(root):
            if not root:
                return 0
            tmp = root.val
            if root.left:
                tmp += h(root.left.left) + h(root.left.right)
            if root.right:
                tmp += h(root.right.left) + h(root.right.right)
            return max(tmp, h(root.left) + h(root.right))        
        return h(root)        
