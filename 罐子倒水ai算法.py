from collections import defaultdict
j1,j2,aim = 4,3,2
visited = defaultdict(lambda:False)
def w(a1,a2):
    if (a1==aim and a2==0)  or (a1==0 and a2 == aim):
        print((a1,a2))
        return True
    if visited[(a1,a2)] == False:
        print((a1,a2))
        visited[(a1,a2)] =True
        return w(0,a2) or\
               w(a1,0) or\
               w(j1,a2) or\
               w(a1,j2) or\
               w(a1+min((j1-a1),a2),a2-min((j1-a1),a2)) or \
               w(a1-min((j2-a2),a1),a2+min((j2-a2),a1))
    else:
        return False


print(w(0,0))
    
