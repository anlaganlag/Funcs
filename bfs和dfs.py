"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans =[]
        q = [root]
        while q:
            n = []
            tmp = []
            for i in q:
                tmp.append(i.val)
                for j in i.children:
                    n.append(j)
            ans.append(tmp)
            q  = n
        return ans

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        def h(n,d):
            if not n:
                return 
            if len(ans) == d:
                ans.append([])
            ans[d].append(n.val)
            for i in n.children:
                h(i,d+1)
        h(root,0)
        return

