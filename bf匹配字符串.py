def bf(t,p):
    n=len(t)
    m=len(p)
    for i in range(n-m+1):
        #n的序列減去m的序列,由於最後是exclude所以+1
        j = 0
        while j <m and  t[i+j] == p[j]:
#i相當於在for循環靜止的但是j在匹配的情況持續增長,這個技巧有點厲害
            j +=1
        if j == m:
            return i
    return -1




