class Solution:
    def maximalRectangle(self, g: List[List[str]]) -> int:
        if not g or not g[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in g] #先将每一行变成2进制的数字
        ans = 0
        for row in range(len(g)):#遍历每一行，求以这一行为第一行的最大矩形
            curRow = row
            while curRow < len(g): #依次与下面的行进行与运算。
                nums[row] &= nums[curRow]  #num中为1的部分，说明上下两行该位置都是1，相当于求矩形的高，高度为j-i+1
                if nums[row]==0: #没有1说明没有涉及第i到第j行的竖直矩形
                    break
                width, curNum = 0, nums[row]
                while curNum: 
                    width += 1
                    curNum  &= (curNum >> 1)
                ans = max(ans, width * (curRow-row+1))
                curRow += 1
        return ans
