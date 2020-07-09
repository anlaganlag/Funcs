"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, n: 'Node') -> 'Node':
        if not n:
            return 
        q = collections.deque()
        q.append(n)
        while q:
            size=len(q)
            p = None#这个是相当于从左边的节点一直移动到最右边的那个节点..
            for i in range(size):#有几个节点就pop几次..
                cur = q.popleft()#每次都是pop最左边的节点..
                                #字面意思和树都是最左边的节点..
                if p:# 由于在每层的一开始强行将p初始化为None..
                    p.next = cur
                    p  = p.next
                    #每次p的next指向下一个节点..
                    #p更新为next..
                else:#所以p开始会变成tree的最左边的节点..
                    p = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            p.next = None
            #这句保证最右边的节点指向None..
        return n
        

