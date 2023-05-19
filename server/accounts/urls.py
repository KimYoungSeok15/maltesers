from django.urls import path
from . import views


urlpatterns = [
    path('userprofile/<str:username>/', views.profile),
    path('followings/', views.follow_list),
    path('followings/<str:username>/', views.following_count),
    path('followers/<str:username>/', views.follower_count),
]
