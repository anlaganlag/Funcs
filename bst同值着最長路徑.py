
#bst中最大路徑和124..
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def h(n):
            nonlocal ans
            if n == None:
                return 0
            l,r = max(h(n.left),0),max(h(n.right),0)
            ans = max(ans,l+r+n.val)
            return max(l,r)+n.val
        ans = float("-inf")
        h(root)
        return ans


#關於最大和..
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            price_newpath = node.val + left_gain + right_gain

            max_sum = max(max_sum, price_newpath)
        
            return node.val + max(left_gain, right_gain)
   
        max_sum = float('-inf')
        max_gain(root)
        return max_sum



class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def h(n):
            nonlocal ans
            if  n == None:
                return 0
#遞歸終止於nil節點...
            l,r = h(n.left),h(n.right)
#找到對應子節點的長度..
            l_=r_=0
#但是默認這些子節點都是0
#只有在子節點存在且..和當前節點相等則+1,並入l_..
            if n.left and n.val==n.left.val:
                l_+=l+1
            if n.right and n.val==n.right.val:
                r_+=r+1
            ans = max(ans,l_+r_)
#隨時更新最大的ans..
            return max(l_,r_)
#但是對於祖父級別的節點只接受最長的一直..
        ans = 0
        h(root)
        return ans
"""
687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
"""
