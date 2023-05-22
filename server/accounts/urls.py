from django.urls import path
from . import views


urlpatterns = [
    path('userprofile/<str:username>/', views.profile), # 프로필 조회, 회원가입 시 프로필 추가
    path('userprofile/user_like_genre/<str:username>/', views.user_like_genre), 
    path('userprofile/user_like_movie/<str:username>/', views.user_like_movie), 
    
    path('userprofile/put/<str:username>/', views.profile_update), # 프로필 갱신(포인트 증감, 프로필사진 수정)
    path('followings/', views.follow_list), # 전체 팔로우 리스트 조회
    path('followings/count/<str:username>/', views.following_count), # 팔로잉 카운트 조회
    path('follow/check/<str:username>/', views.follow_check), 

    path('Likes/', views.likes), #좋아요 전체 목록
    path('Likes/<str:username>/', views.user_likes), # 특정 유저가 좋아요 한 영화 목록
]