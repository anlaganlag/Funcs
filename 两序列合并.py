lst1=[1,2,4]
lst2=[0,1,3]
def mg(l1,l2):
"""用的是3三个指针的思维"""
    m = len(l1)
    n = len(l2)
    cur=l1 + n*[0]
    px= m+n-1
    p1=m-1
    p2=n-1
    while p1 >-1 and p2 >-1:
#         print(p1,p2)
        if l2[p2] > l1[p1]:
            cur[px] =l2[p2]
            p2-=1
            px-=1
        else:
            cur[px] =l1[p1]
            p1-=1
            px-=1
    if p2> -1:
        cur[:p2+1] = l2[:p2+1]
    return cur

#两个排序好的序列合并

