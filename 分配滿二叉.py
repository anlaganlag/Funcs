
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        memo = {0: [], 1: [TreeNode(0)]}
        
        def get_FBT(n):
            if n in memo:
                return memo[n]
            res = []
            for x in range(n):
                y = n - 1 - x
                for left in get_FBT(x):
                    for right in get_FBT(y):
                        p = TreeNode(0)
                        p.left = left
                        p.right = right
                        res.append(p)
            memo[n] = res
            return res

        get_FBT(N)
        return memo[N]




class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N & 1 == 0:
           return []
        dp = [[] for _ in range(N+1)]
        dp[1] = [TreeNode(0)]
        for j in range(3, N+1, 2):
           res = []
           for x in range(1, j, 2):
               y = j - 1 - x
               for left in dp[x]:
                   for right in dp[y]:
                       p = TreeNode(0)
                       p.left = left
                       p.right = right
                       res.append(p)
           dp[j] = res
        return dp[N]

     
