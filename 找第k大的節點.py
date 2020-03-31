class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def h(n):
            nonlocal res,k
            if not n:
                return
            h(n.right)
            k-=1
            if not k:
                res = n.val
            if k :
                h(n.left)
        ans = None
        h(root)
        return ans

