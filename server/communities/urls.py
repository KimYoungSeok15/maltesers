from django.urls import path
from . import views


urlpatterns = [
    path('freeboards/', views.freeboard_list),
    path('freeboards/<int:freeboard_id>/', views.freeboard_detail),
    path('reviewboards/', views.reviewboard_list),
    path('reviewboards/<int:reviewboard_id>/', views.reviewboard_detail),
]