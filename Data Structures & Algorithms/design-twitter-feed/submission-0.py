from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # User should always see their own tweets
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]

            if tweets:
                index = len(tweets) - 1
                count, tweetId = tweets[index]

                # negative count because Python heapq is min-heap
                heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])

        while maxHeap and len(res) < 10:
            negCount, tweetId, followeeId, nextIndex = heapq.heappop(maxHeap)
            res.append(tweetId)

            if nextIndex >= 0:
                count, nextTweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(maxHeap, [-count, nextTweetId, followeeId, nextIndex - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Usually, unfollowing yourself should not break news feed behavior.
        # But even if removed, getNewsFeed adds self back.
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)