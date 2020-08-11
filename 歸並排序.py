def ms(l):
    if len(l)<2:
        return l
    mid = len(l)//2
    L = ms(l[:mid])    
    R = ms(l[mid:])
    return merge(L,R)
def merge(l,r):
    ans = []
    while l and r:
        ans.append(l.pop(0)) if l[0]<r[0] else ans.append(r.pop(0))
#py也可以用二元真的爽.
    return ans+l+r


//用兩個指針..
def merge(l,r):
    ans = []
    p=q=0
    while p <len(l) and q<len(r):
        if l[p]<r[q]:
            ans.append(l[p])
            p+=1
        else:
            ans.append(r[q])
            q+=1
    ans+=l[p:]+r[q:]
    return ans

