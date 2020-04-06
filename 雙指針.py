class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        p,q = 0,len(s)-1
        o = 'aeiouAEIOU'
        while p<q:
            if l[p] not in o:
                p+=1
            if l[q] not in o:
                q-=1
            if l[p] in o and l[q] in o:
                l[p],l[q] = l[q],l[p]
                p+=1
                q-=1
        return ''.join(l)

"""
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
"""
