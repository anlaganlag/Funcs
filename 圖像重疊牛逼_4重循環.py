class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        d = len(A)
        ans = 0
        for row in range(d):
            for col in range(d):
                o1=o2 =0
                for y in range(d-row):
                    for x in range(d-col):
                        o1 += A[y][x]*B[y+row][x+col]
                        o2 += B[y][x]*A[y+row][x+col]
                ans = max(ans,o1,o2)
        return ans
                        


        
