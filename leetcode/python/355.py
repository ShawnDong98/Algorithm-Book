from collections import defaultdict, OrderedDict
class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self._follow = defaultdict(set)
        self.time = 0
 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        res.extend(self.tweet[userId])
        for user in self._follow[userId]:
            res.extend(self.tweet[user])
        res = sorted(res, key=lambda x: x[1], reverse=True)
        res = [r[0] for r in res[:10]]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if len(self._follow[followerId]) == 0: return 
        self._follow[followerId].remove(followeeId)
