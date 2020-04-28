class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = collections.defaultdict(int)   
        # step1     
        for i,j in dominoes:
            num = 10 * i + j if i < j else 10 * j+ i
#这个牛逼..
#还有一种选择是
#d[10*max(i) +min(i)] +=1

`
            d[num] += 1
        # step2
        for k in d.values():
            ans += int(k*(k-1)/2)
        return ans


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i in dominoes:
#直接排序后思路显得更清晰..
            i.sort()
            d[10*i[0]+i[1]] +=1
        ans = 0
        for i in d.values():
            ans +=i*(i-1)//2
        return ans

