"""
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
	#思路就是將right存儲起來,left放在right,最後接上right..
        def help(n):
            if not n:
                return
            l,r = help(n.left),help(n.right)
            if n.left:
                tmp = n.right
                n.right = n.left
                n.left = None
                while n.right:
                    n = n.right
                n.right = tmp

        return help(root)

