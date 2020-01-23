def p(t):
    """檢查括號是都是匹配的情況,最好是用stack的數據結構
       首先有分清所有的情況
           1> 有開無閉 有(  但是沒有) 有opening 無closing
           2> 鏡像的   有)  但是沒有(..
           3>  有開有閉但是存在交叉  ( [ ) ]
    """
    stack = []#其實就是用列表模擬stack,列表尾部/top
              #對於stack來說所有的數據結構都是在尾部操作
              #append就是相當於push
              #[-1]相當於讀取top
              #pop就是pop
    for i in t:
        if i not in "( ) [ ] { }".split():
        #非括號都直接跳過,不予檢查
            continue
        elif i in "( [ {".split():
            #如果遇到opening的情況,push進stack
            stack.append(i)
        elif i in ") ] }":
            #如果遇到的是closing的情況,
            if len(stack) <1:
                #且stack爲空,即先出現的closing,返回錯誤2
                return("type2 No Opening brace beforehand")
            elif stack[-1]+i not in "() [] {}".split():
                #如果stack不爲空需要比較top和cloing是否匹配,不匹配就是type3
                return("type3 No matching brace happend")
            else:
                #如果是closing且匹配的情況,將top的opening彈出
                stack.pop()
    if len(stack)>0:#如果迭代完畢之後,還有opening剩餘
        return('type1 No Closing brace to match')
    return True
tn="0{abc}{de}(f)[(g)]9"

t0="{abc}{de}(f)[(g) "
t1="f(d)2"
t2="f(d2"
t3="fd)2"
t4="f([d)x]2"
t5='([<^>x[ ]{a}]{/}{t}g<^>)<{x}b>{x}<z({%}w >[b][c[c]]{<h>{h}}'
print(p(tn)) #T
print(p(t0)) #F

print(p(t1)) #True
print(p(t2)) #F
print(p(t3)) #F
print(p(t4)) #F
print(p(t5)) #F


