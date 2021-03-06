class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:       
        def dfs(n):
            if not n:
                return 
            dfs(n.left)
            r = TreeNode(n.val)
            ans.append(r)
            dfs(n.right)
        ans = []
        dfs(root)
        if ans:
            curr=start=TreeNode(None)#两标签都贴在一个None节点，即有两个名字
            for node in ans:
                curr.left = None
                curr.right = node
                curr = node
            return start.right
"""
897. 递增顺序查找树

给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9  
"""
