
"""
355. 设计推特
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户

"""


"""
這個是大神解法用的是set和deque雙端隊列..
所有都共用t..,即無論是自己還是被關注的人都是共用同一個t..
"""
from itertools import islice
class Twitter:
    def __init__(self):
        self.e  = collections.defaultdict(set)
        self.q = collections.defaultdict(collections.deque)
        self.t = 0     
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t +=1
        self.q[userId].appendleft((self.t,tweetId))       
    def getNewsFeed(self, userId: int) -> List[int]:
        userId not in self.e[userId] and self.e[userId].add(userId)
        return [
            v for _,v in islice(heapq.merge(
                *map(self.q.__getitem__,self.e[userId]),
                reverse = True),0,10)
        ]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.e[followerId].add(followeeId)      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.e[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
