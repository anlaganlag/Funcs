class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l = [ListNode(i) for i in range(10)]
l1=ListNode(8)
l1.next = ListNode(7)
l1.next.next = ListNode(8)
l2=ListNode(6)
l2.next = ListNode(5)
l2.next.next = ListNode(9)
def ad(l1,l2):
    st =cur= ListNode(0)  
    c = 0          
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        tmp = a + b +c             
        c = tmp // 10                
        cur.next = ListNode(tmp % 10)  
        if l1:                           
            l1 = l1.next       
        if l2:                        
            l2 = l2.next
        cur = cur.next                 
    if c :                      
        cur.next = ListNode(1)
    return st.next
#878
#659
k=ad(l1,l2)
print(k.val,k.next.val,k.next.next.val,k.next.next.next.val)



