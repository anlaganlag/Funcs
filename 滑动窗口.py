
def findSubstring(s):
    N = len(s)
    left,right = 0,0
    counter = collections.Counter()
    res = 0
    while right < N:
        counter[s[right]] +=1
        #while [left,right] 不符合题意。。
        #此时需要一直移动left
            counter[s[left]] -=1
            left +=1
        res = max(res,right-left+1)
        right +=1
    return res
    

