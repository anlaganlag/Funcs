# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums) :     
	"""�õݹ�ط�ʽ������,�е�����binary sort
	  ���е������������ʽ

	����˼ά�������б���е�ѡһ��root�ڵ�,odd�е�,even�м������ұ��Ǹ�Ԫ��
	ѡ��root���ڵ��ݹ�Ķ���left��right

       ��󷵻�root����




	"""
    if nums:
        n =len(nums)
        mid = n//2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+1:])
        return root
# ����
List=[-10,-3,0,5,9]


