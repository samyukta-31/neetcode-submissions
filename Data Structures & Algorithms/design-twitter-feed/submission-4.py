class Twitter:

    def __init__(self):
        import heapq
        self.users = {}
        self.follows = {}
        self.i = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.i += 1
        if userId in self.users:
            self.users[userId].append((self.i, tweetId))
        else:
            self.users[userId] = [(self.i, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        self.heap = []
        import heapq
        heapq.heapify(self.heap)
        follows = self.follows.get(userId, set())
        all_users = list(follows) + [userId]
        for user in all_users:
            for tweet in self.users.get(user, []):
                heapq.heappush(self.heap, tweet)
                if len(self.heap) > 10:
                    heapq.heappop(self.heap)
        sorted_tweets = sorted(self.heap, key = lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in sorted_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)  
        else:
            self.follows[followerId] = set()
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
