"""
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""
class Solution:
    def sortList(self, n: ListNode) -> ListNode:
        def merge(l1, l2):#兩個鏈表合並
            if not l1 :
                return l2
            if not l2:
                return l1

            if l1.val <= l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        def mergeSort(n):#對鏈表進行歸並排序
            if not n  or not n.next:#如果只有一個或者爲None 返回當前節點 即base case
                return n

            pre = n #慢節點
            cur = n.next#快節點
            while cur and cur.next:
                pre = pre.next#慢節點每次前進一步
                cur = cur.next.next#快節點每次前進兩步
            #此時快節點到達尾部最後,或者是None,比如兩個就是最後,三個None
            #而慢總是在偏左(偶數)或者是中間的位置(奇數)

            mid = pre.next      #第二部分鏈表
            pre.next = None   
            l1 = mergeSort(n)
            l2 = mergeSort(mid)
            ans = merge(l1, l2)
            return ans

        return mergeSort(n)
