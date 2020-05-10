class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length=len(s)
        if length==0:
            return ""
        rs = s[::-1]
        i = 0
        while True:
            if rs[i:]==s[:length-i]:
#簡單來說就是舍去後面幾位的部分是回文..
                break
            i+=1
        return rs[:i]+s
#舍去的幾位補上..


"""
214. 最短回文串
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"
"""
