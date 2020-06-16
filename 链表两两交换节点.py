    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#经典的节点问题..
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(tmp.next)#这里核心代码
        #head节点的下一个节点的可以递归的解决
        #但是由於head.next被覆蓋,所以在前面要將head存儲到一個變量比如tmp
        tmp.next = head#利用tmp節點完成了交換
        #即交換其實是超級簡單的代碼 a->b則交換就是b->a
        return tmp

