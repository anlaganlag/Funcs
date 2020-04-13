
#超級聰明的雙指針..
#j指針只要不等於val就將其依次放在首位...
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0;
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
#由於找到第一個元素的時候是1,所以找到n個的時候是就是n
        return i




#前一種方法就是將不同的元素丟在開頭
#這種方法類似將相似的元素丟在隊尾部..,再幹掉
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0;
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n-=1
            else :
                i+=1
        return n
