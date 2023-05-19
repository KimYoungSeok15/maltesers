from django.urls import path
from . import views


urlpatterns = [
    path('freeboards/', views.freeboard_list), # 자유게시판 전체 리스트
    path('freeboards/<int:freeboard_id>/', views.freeboard_detail), # 자유게시판 글 아이디로 자유게시판 디테일 보기
    path('reviewboards/', views.reviewboard_list), # 전체 리뷰 리스트
    path('reviewboards/<int:reviewboard_id>/', views.reviewboard_detail), # 리뷰 아이디로 리뷰 디테일 
    path('reviewboards/<str:related_movie_title>/', views.reviewboard_related_movie), # 영화 이름으로 리뷰 검색
    path('freeboards/<str:search_keyword>/', views.search_freeboard_list), # 자유게시판 글 검색
]