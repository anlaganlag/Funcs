# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums) :     
	"""用递归地方式定义树,有点类似binary sort
	  有有点类似链表的形式

	形象化思维就是在列表的中点选一个root节点,odd中点,even中间间隔的右边那个元素
	选好root根节点后递归的定义left和right

       最后返回root即可




	"""
    if nums:
        n =len(nums)
        mid = n//2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        return root
# 输入
List=[-10,-3,0,5,9]


