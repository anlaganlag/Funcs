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






"""
2020,01,30重新revist並添加了注釋

t1,t2= "THIS IS A TEST TEXT","AABAACAADAABAABA"
p1,p2= "TEST","AABA"
def bf(t,p):
#text 和 patter
#或者是說模式pattern  和 target
#這裏用的是前者
    n,m = len(t),len(p)
    done = False
    for i in range(n-m+1):
        #對於text來說總是從0開始的,一直到最後的n-m的位置,但是text遍歷的位置
        #這裏爲什麼要+1主要是因爲是閉空間,左開右閉的樣子
        j = 0
        #就是pattern總是要從0開始匹配的
        while j < m and t[i+j] == p[j]:
    #   當j沒有到達最後   i相當於是靜止或者說是常數,j就是遞增的
            j +=1
        if j==m:
            done = True
            print(i)
    return done
print(bf(t1,p1))
print(bf(t2,p2))

"""



