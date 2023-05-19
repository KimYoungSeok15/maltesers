from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
# from .serializers import FreeboardListSerializer, ReviewboardListSerializer
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Following, Profile
from .serializers import ProfileSerializer, followingListSerializer



# Create your views here.
@api_view(['GET', 'POST'])
def profile(request, username):
    if request.method == 'GET':
        user_profile = get_object_or_404(Profile, user_name=username)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# 팔로우 전체 목록 조회  
@api_view(['GET'])
def follow_list(request):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following)
        serializer = followingListSerializer(user_follow, many=True)
        return Response(serializer.data)
        
# 사용자를 팔로우한 사람 숫자 보내기
@api_view(['GET'])
def following_count(request, username):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following, following=username)
        user_following_count_json = []
        user_following_count_json.append(
            {
            "following_count": len(user_follow),
            }
        )   
        return JsonResponse(user_following_count_json, safe=False)
    
        
# 사용자가 팔로잉한 사람 숫자 보내기
@api_view(['GET'])
def follower_count(request, username):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following, user_name=username)
        user_following_count_json = []
        user_following_count_json.append(
            {
            "following_count": len(user_follow),
            }
        )   
        return JsonResponse(user_following_count_json, safe=False)
        