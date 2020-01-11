
ar= [2,33,17,25,6,12]
#冒泡排序
def b(ar):
    """bubble 排序的的核心在於最大數字會到最後,即每次能確定最後一位
        依靠的是每次選兩者較大的那個數排在後面,然後繼續兩兩比較,每次都是大數在後,就保證了
        最大的數能流動到最後,即確定了最後一位(n-1)
        以此類推確定..到第1位
    """
    n= len(ar)
    lst = ar[:]
    for comfirm_digit in range(n-1,0,-1):
    #冒泡排序首先的確定最後一位的位置,即n-1
#             然後是是確定n-2,倒數第二位
#                    ..
#             最後是確定1位置
#             第0位不需要確定
        for compare in range(comfirm_digit):
            if lst[compare]>lst[compare+1]:
                lst[compare],lst[compare+1] = lst[compare+1],lst[compare]
                #即較大的數字的index變成了compare+1
                #而在for循環中下一個compare也是compare+1,即compare+1(較大的數字)繼續參與比較
                #即較大的數字繼續bubble
    return lst
print(b(ar))
