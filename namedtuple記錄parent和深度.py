from collections import namedtuple
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        node_id = namedtuple('node_info',['level','parent'])        
        def dfs(node,level,parent):
            if not node:
                return 
            if node.val == x:
                self.n_x = node_id(level=level,parent=parent)
            if node.val == y:
                self.n_y = node_id(level=level,parent=parent)
            dfs(node.left,level+1,node)
            dfs(node.right,level+1,node)        
        dfs(root,0,None)
        return self.n_x.level == self.n_y.level and self.n_x.parent != self.n_y.parent
        
