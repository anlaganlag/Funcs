class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        m = []
        def h(n,i):
            if n:
                m.append(i)
                h(n.left,2*i)
                h(n.right,2*i+1)
        h(root,1)
        return max(m) == len(m)
#參考別人的答案,其實思路簡單
#別人用到的技巧就是
#i<<1 相當於乘以2
#對偶數|1 求 or 即對偶數+1,花裏胡哨的




self.red_left, self.red_right = 0, 0
def dfs(root):
    if not root:
	return 0
    left = dfs(root.left)
    right = dfs(root.right)
    if root.val == x:
	self.red_left = left
	self.red_right = right
    return left + right + 1

dfs(root)
parent = n - self.red_left - self.red_right - 1
judge = [parent, self.red_left, self.red_right]
return any([j > n // 2 for j in judge])
