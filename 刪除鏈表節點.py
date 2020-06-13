# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
#將啞節點和pre都設置爲None
        dummy = pre = ListNode()
#呀節點和當前節點設置爲head節點..
        dummy.next=cur = head
#找到要刪除的節點
        while cur.val != val:
            pre,cur = cur,cur.next
#繞過cur節點..
        pre.next = cur.next
        return dummy.next
#返回dummy.next
