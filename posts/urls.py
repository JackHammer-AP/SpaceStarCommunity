from django.urls import re_path
from . import views

app_name = 'posts'

urlpattern = [
    re_path(r'',views.PostList.as_views(),name='all'),
    re_path(r'^new/$',views.CreatePost.as_views(),name='create'),
    re_path(r'^by/(?P<username>[-\w]+)/$',views.UserPosts.as_views(),name='for_user'),
    re_path(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_views(),name='single'),
        re_path(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_views(),name='delete'),
]
