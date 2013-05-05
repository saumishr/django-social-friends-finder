from django.conf.urls import *
from social_friends_finder.views import FriendListView, FriendListViewAll, send_app_request
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('social_friends_finder.views',
    url(r'^list/$', login_required(FriendListView.as_view()), name='friend_list'),
    url(r'^list/(?P<provider>[\w.@+-]+)/$', login_required(FriendListView.as_view()), name='friend_list'),
	url(r'^listAll/$', login_required(FriendListViewAll.as_view()), name='friend_list_all'),
)
