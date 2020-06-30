def bar(n):
    ans =0
    while n:
        ans = ans*10+n%10
        n//=10
    return ans
import random
x=random.randint(1,10000000)
print(x)
bar(x)

#取頭取尾真的是太牛逼了
def foo(x):
    if x<0:
        return False
    div =1#除數等於1
    while x//div >=10:
        div *=10
    while x:
        l = x//div
        r = x%10
        if l != r:
            return False
        x = (x % div) //10
        div //= 100
    return True
foo(906271172609)
