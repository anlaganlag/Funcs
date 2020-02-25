#終於弄清楚大神的解法一些不太清楚的地方
def longest_palindrome(s):
	"""求字符串中最長的回文子串,用的中心拓展的思路,中心的要求是單字母,或者是疊字比如xx這個樣子,這兩種情況都可以分別用A(s,i,i)和A(s,i,i+1)表示"""
    max_,n = '', len(s)
    A = lambda s,l,r:A (s,l-1,r+1) if l-1>=0 and r+1<n and s[l-1] == s[r+1] else s[l:r+1]
#這裏主要是用了lambda調用的遞歸函數,即每個A(s,l,r) 在滿足if後都會
#遞歸地調用A(s,l-1,r+1)直到不滿足if返回切片
#即這裏是中心擴展的思想從中心點開始
		#判斷邊界條件
        #判斷最外一個字符是否相等
		#..
        #如果出現不相等,或者到達邊距,則不再調用函數本身,返回已經匹配的部分s[l,r+1]

    if len(set(s))== 1:
        return s
#這裏主要是處理多個相同字母的情況,如果set==1,那麼就是回文序列
    for i in range(n):
        #t1,t2 = A(s,i,i),A(s,i,i+1) if i+1 <n and s[i] == s[i+1] else ''
        t1= A(s,i,i)
        t2 = A(s,i,i+1) if i+1 <n and s[i] == s[i+1] else ''
#其實就是分別賦值
          #a ,b  = x1 ,x2
   #前後是一一對應的 a 接受x1的賦值
                     #b     x2的if..else
#即if和else只對b發生作用
        max_ = max(max_,t1,t2,key=len)
#這裏由於max_,t1,t2都是字符串,用key=len,即字符串最長的將會傳入max_變量
#比如字符串相等,則不會發生賦值
    #這裏還有一個比較牛逼的地方就是max_,t1,t2三方求max操作
    #即最長的字符串會保存在max_裏面
    return max_

#大神思路就是大神思路,牛逼
#這個思路就是中心拓展+遞歸地比較最外的一個字符


