class SocialMediaAccount:
    def __init__(self, username, password): 
        self.username = username
        self.password = password
    
    def describeAccount(self):
        print(f"Username: {self.username}\nPassword: {self.password}\n")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, num_followers):
        super().__init__(username, password)
        self.num_followers = num_followers
    
    def igAccount(self):
        print(f"Username: {self.username}\nNumber of followers: {self.num_followers}")
    
    def shareStory(self):
        print(f"{self.username} shared a story\n")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, num_tweets):
        super().__init__(username, password)
        self.num_tweets = num_tweets
    
    def twtAccount(self):
        print(f"Username: {self.username}\nNumber of tweets: {self.num_tweets}")
        
    def tweet(self):
        print(f"{self.username} posted a new tweet\n")
    
aries_ig = InstagramAccount("aries", "123", 2)
aries_twt = TwitterAccount("aries", "123", 3)

aries_ig.describeAccount()
aries_ig.igAccount()
aries_ig.shareStory()
aries_twt.twtAccount()
aries_twt.tweet()