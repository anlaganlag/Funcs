l1= [7,3,1,13]
def bubble_sort(ar):
	"""思路很简单就是
		i是记录最后一位排序完成的情况0就是最后一位
		一直冒泡到倒数第二位,不会超出数组范围所以j是范围-1
		最后一次比较是0和1比较,所以j要留下1
		所以i也是n-1,应为i第一位是0,所以最后j还有1
	"""
		
    n = len(ar)
    for i in range(n-1):
        for j in range(n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]
    return ar


# bubble_sort(l1)

# [1, 3, 7, 13]
