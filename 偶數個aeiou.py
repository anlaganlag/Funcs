class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
#由於有aeiou5個字母,則有2**5種情況..從全00000到全11111
				     #全部爲偶數 #全爲奇數個
#即共有32種情況..
        ans=status=0
        p=[0]+31*[-1]
#p用來記錄這32種情況出現的..初始化的時候只有第一位是0,即index爲0時爲偶數種情況..這裏選擇的是從1開始計數..
        for i,v in enumerate(s,1):
            if v in 'aeiou':
                status ^=1<<'aeiou'.index(v)
#每次出現aeiou的就更新status..
#首次出現則記錄idx...
            if p[status] == -1:
                p[status] = i
            else:
#如果再次出現則則說明出現了00000的情況..
                ans = max(ans,i-p[status])
        return ans
"""
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
"""
