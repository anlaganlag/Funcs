"""
面试题 17.22. 单词转换
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        patterns = collections.defaultdict(list)#用wordList不如用pattern表示更好
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                patterns[word[:i] + '*' + word[i + 1:]].append(word)#存储patterns对应的单词否是字典
                #字典词抽象成patterns，符合patterns词之间可以一步到位。。

        queue = collections.deque([beginWord])#没有出现的个放在queque队列里面
        w_dict = {beginWord: [beginWord]}#从起点到对应单词的路线，pathway
        while queue:
            word = queue.popleft()
            if word == endWord:
                return w_dict[word]
            for i in range(n):
                pattern= word[:i] + '*' + word[i + 1:]
                if  pattern in patterns:
                    for candidate in patterns[pattern]:
                        if candidate not in w_dict:
                            w_dict[candidate] = w_dict[word] + [candidate]
                            queue.append(candidate)
        return []


