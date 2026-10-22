from functools import wraps

class Twitter:

    timestamp = 0

    def get_timestamp(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.timestamp += 1
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        
    @get_timestamp
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        candidates = []

        for u in self.followers[userId] | {userId}:
            
            candidates.extend(self.tweets[u][-10:])
            candidates.sort(key=lambda x: x[0], reverse=True)
        return [tweet_id for _, tweet_id in candidates[:10]]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)






        
