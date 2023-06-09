# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_id>/comments/', views.comment_create),
    path('movies/genres/', views.all_genres), # 전체 장르 보내기
    path('movies/genrename/', views.movie_genrename), # 해당 영화 장르 이름 보내기
]
