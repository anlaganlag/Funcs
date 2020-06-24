"""
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

"""


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        def h(n,k):
            nonlocal s
            if not n:
                return False
            if n.val in s:#如果当前书等于互补数,证明和前面的互补..
                return True
            s.add(k-n.val)#存放互补数..
            return h(n.left,k) or h(n.right,k)
        return h(root,k)

#用bst..注意如果是nil节点..就弹出..
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        q = collections.deque()
        q .append(root)
        while q:
            if not q[0] :
                q.popleft()
            else:
                node = q.popleft()
                if k-node.val in s:
                    return True
                s.add(node.val)
                q.extend([node.left,node.right])
        return False
