
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#l是所謂的累計數組記錄從root(level0)到當前節點..level1到當前節點..一直當前節點的和..
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        def dfs(n, l):
            if not n:
                return 0
            l = [_+n.val for _ in l]#從root(level0)的到當前節點前都加上當前節點

            l.append(n.val)
            return l.count(s) + dfs(n.left, l) + dfs(n.right, l)

        return dfs(root, [])



