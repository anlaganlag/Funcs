class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left #左边
            root = stack.pop()
            ans.append(root.val)#
            root = root.right
        return ans


