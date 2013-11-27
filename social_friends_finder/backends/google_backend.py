from social_friends_finder.backends import BaseFriendsProvider
from social_friends_finder.utils import setting
if not setting("SOCIAL_FRIENDS_USING_ALLAUTH", False):
    from social_auth.backends.google import GoogleOAuth2Backend
    USING_ALLAUTH = False
else:
    from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
    USING_ALLAUTH = True

from xml.etree import ElementTree
from social_auth.backends import google
import requests

# see: http://djangosnippets.org/snippets/706/
class GoogleFriendsProvider(BaseFriendsProvider):

	def fetch_friends(self, user):
		return None

	def import_contacts(self, user):
		if USING_ALLAUTH:
			social_app = SocialApp.objects.get_current('google')
			oauth_token = SocialToken.objects.get(account=user, app=social_app).token
		else:
			social_auth_backend = GoogleOAuth2Backend()

			# Get the access_token
			tokens = social_auth_backend.tokens(user)
			oauth_token = tokens['access_token']

		response = requests.get(google.CONTACTS_URL + '?access_token=' + oauth_token)
		return self.parse_contacts(response.text)

	def parse_contacts(self, contacts_xml=None):
		tree = ElementTree.ElementTree(ElementTree.fromstring(contacts_xml.encode("utf-8")))
		root = tree.getroot()
		elms = root.findall("{http://www.w3.org/2005/Atom}entry")
		contacts = []

		for elm in elms:
			children = elm.getchildren()
			for child in children:
				if child.tag == "{http://schemas.google.com/g/2005}email":
					contacts.append(child.attrib.get('address'))

		return contacts

	def fetch_friend_ids(self, user):
		return []
