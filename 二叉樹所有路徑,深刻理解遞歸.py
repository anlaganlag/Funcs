def b(root):
    def h(n,l):
        if not n:
            return []
        l += str(n.val)             
        if not n.left and not n.right:
            paths.append(l)                          
        l+="->"
        h(n.left,l)
        h(n.right,l)
        return paths
    paths = []
    return h(root,"")


"""
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


"""


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def h(n):
            if not n:
                return []
            l = []
            q = [(n,str(n.val))]
            while q:
                c,s =q.pop()
                if not c.left and not c.right:
                    l.append(s)
                if c.left:
                    q.append((c.left,s+'->'+str(c.left.val)))
                if c.right:
                    q.append((c.right,s+'->'+str(c.right.val)))
            return l
        return  h(root)
