# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class FindElements:
    def __init__(self, root: TreeNode):
        self.elems = defaultdict(int)
        def dfs(node, val):
            if not node:
                return
            node.val = val
            self.elems[val] = True
            dfs(node.left, val * 2 + 1)
            dfs(node.right, val * 2 + 2)
        dfs(root, 0)
    def find(self, target: int) -> bool:
        return self.elems[target]


        


