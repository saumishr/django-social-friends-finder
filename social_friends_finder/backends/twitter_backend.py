from social_friends_finder.backends import BaseFriendsProvider
from social_auth.backends.twitter import TwitterBackend
from django.conf import settings
import twitter

class TwitterFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        fetches the friends from twitter using the
        information on django-social-auth models
        user is an instance of UserSocialAuth

        Returns:
            collection of friend objects fetched from facebook
        """
        t = TwitterBackend()

        # Fetch the token key and secret
        tokens = t.tokens(user)
        oauth_token_secret = tokens['oauth_token_secret']
        oauth_token = tokens['oauth_token']

        # Consumer key and secret from settings
        consumer_key = settings.TWITTER_CONSUMER_KEY
        consumer_secret = settings.TWITTER_CONSUMER_SECRET

        # now fetch the twitter friends using `python-twitter`
        api = twitter.Api(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=oauth_token,
                access_token_secret=oauth_token_secret
        )
        return api.GetFriends()

    def fetch_friend_ids(self, user):
        """
        fethces friend id's from twitter

        Return:
            collection of friend ids
        """
        friends = self.fetch_friends(user)
        friend_ids = []
        for friend in friends:
            friend_ids.append(friend.id)
        return friend_ids
