# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def h(n):
            if not n:
                return 0
            return max(h(n.left),h(n.right))+1
        def p(n,lv,st,mv):
            if not n:
                return 
            if lv == row:
                return 
            s[lv][st] = str(n.val)
            p(n.left,lv+1,st-mv,mv//2)
            p(n.right,lv+1,st+mv,mv//2)
        row = h(root)
        col = (1<<row)-1
        s = [['' for i in range(col)] for j in range(row)]
        p(root,0,(col-1)//2,(col+1)//4)
        return s
#(col-1)//2是在找字符串的中點位置
#(col+1)//4是在左右數分別向左右移動的距離.. 
        
