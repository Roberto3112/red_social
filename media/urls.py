from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(feed), name='feed'),
    path('post_action', post_action,name='post_action'),
    path('settings/', login_required(settings), name='settings'),
    path('profile/<int:id>', login_required(profile_view), name='profile_view'),
    path('profile/post_action', post_action, name='profile_post_action'), 
    path('post/<int:id>/comment', login_required(add_comment_to_post), name='add_comment'),
    path('comment_action', login_required(comment_action), name='comment_actions')
]
