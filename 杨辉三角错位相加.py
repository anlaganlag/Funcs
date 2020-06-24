class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: 
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
#错位相加
            res.append(newRow)      
        return res


