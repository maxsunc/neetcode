class Twitter:

    def __init__(self):
        # initialize the twitter object

        # find who each person follows dictionar <int, list<int>>
        self.followDict = defaultdict(set)
        # the posts that each user made dictionary <int, list<int>
        self.postDict = defaultdict(list) # list of (timePosted, tweetId)
        self.timePosted = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # make an ew tweet and tweetId by userId
        # tweetId is Unique
        # userId tweets tweetId
        self.timePosted += 1
        entry = (self.timePosted, tweetId)
        self.postDict[userId].append(entry) 
        # store a post we need to track the frame it was posted


    def getNewsFeed(self, userId: int) -> List[int]:
        # fetches at most the 10 most recent tweet ID's in the user's new feed
        # must be tweets from users following or by themselves
        # ordered from most recent to least recent

        # hardest method to implement
        # information we have: people userId is following
        # the posts made by those users
        # 1. compile all the posts made by followed users and yourself and their time completed
        tweets = []
        # Must include self
        followees = self.followDict[userId] | {userId}
        for followee in followees:
            posts = self.postDict[followee]
            for post in posts:
                tweets.append(post)

        # 2. change it into a max heap O(n) - n = number of posts by people following and yourself
        heapq._heapify_max(tweets)
        # 3. get the top 10 elements and put into result
        res = []
        for i in range(0,10):
            if not tweets:
                break
            res.append(heapq._heappop_max(tweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # user with followerId follows user with followeeId
        if followerId != followeeId:
            self.followDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # user with followerId unfollows user with followeeId
        if followeeId in self.followDict[followerId]:
            self.followDict[followerId].remove(followeeId)