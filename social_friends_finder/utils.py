from django.conf import settings


class SocialFriendsFinderBackendFactory():

    @classmethod
    def get_backend(self, backend_name):
        """
        returns the given backend instance
        """
        if backend_name == 'twitter':
            from social_friends_finder.backends.twitter_backend import TwitterFriendsProvider
            friends_provider = TwitterFriendsProvider()
        elif backend_name == 'facebook':
            from social_friends_finder.backends.facebook_backend import FacebookFriendsProvider
            friends_provider = FacebookFriendsProvider()
        elif backend_name == 'vkontakte-oauth2':
            from social_friends_finder.backends.vkontakte_backend import VKontakteFriendsProvider
            friends_provider = VKontakteFriendsProvider()
        elif backend_name == 'google-oauth2' or backend_name == 'google-oauth' or backend_name == 'google':
            from social_friends_finder.backends.google_backend import GoogleFriendsProvider
            friends_provider = GoogleFriendsProvider()
        else:
            raise NotImplementedError("provider: %s is not implemented")

        return friends_provider


def setting(name, default=None):
    """returns the setting value or default if not exists"""
    return getattr(settings, name, default)
