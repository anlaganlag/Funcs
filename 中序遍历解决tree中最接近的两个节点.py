class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
prev = float('-inf')
ans = float('inf')
def minDiffInBST(root):    
    def dfs(node):
        global ans,prev
        if node:
            v =node.val
            dfs(node.left)
            ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)

    dfs(root)
    return ans
#           4
#         /   \
#       2      6
#      / \    
#     1   3  

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t6=TreeNode(6)
t4.left=t2
t4.right=t6
t2.left=t1
t2.right=t3
print(minDiffInBST(t4))


