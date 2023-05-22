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
from .models import Following, Profile, UserLikeGenre, UserLikeMovie
from .serializers import ProfileSerializer, followingListSerializer, UserLikeGenreSerializer, UserLikeMovieSerializer


# Create your views here.
# 프로필 정보 출력
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


        
# 유저 정보 갱신(포인트갱신, 프로필 수정)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile_update(request, username):
    try:
        user_profile = Profile.objects.get(user_name=username)
    except Profile.DoesNotExist:
        return Response({'error': 'User profile not found.'}, status=404)
    print(request.FILES)
    user_name = request.data.get('user_name')
    date_joined = request.data.get('date_joined')
    point = request.data.get('point')
    profile_pic = request.FILES.get('file')
    print(profile_pic)
    if user_name:
        user_profile.user_name =  user_name
    if date_joined:
        user_profile.date_joined = date_joined
    if point:
        user_profile.point = point
    if profile_pic:
        user_profile.profile_pic = profile_pic

    user_profile.save()
    serializer = ProfileSerializer(user_profile)
    return Response(serializer.data)
    
    

# 팔로우 전체 목록 조회, 팔로우 관계 추가  
@api_view(['GET', 'POST'])
def follow_list(request):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following)
        serializer = followingListSerializer(user_follow, many=True)
        return Response(serializer.data)

    else:  # POST 요청일 경우
        # 기존에 동일한 팔로우 관계 있는지 확인하고 저장해야 함
        user_name = request.data['user_name']
        following = request.data['following']
        user_follow = Following.objects.filter(user_name=user_name, following=following)

        if user_follow.exists():
            return Response({'error': '이미 팔로우한 사용자입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if user_name == following:
            return Response({'error': '자기 자신을 팔로우할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = followingListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
# 사용자를 팔로우한 사람 숫자 보내기
@api_view(['GET'])
def following_count(request, username):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following, following=username)
        serializer = followingListSerializer(user_follow, many=True)
        user_following_count_json = []
        user_following_count_json.append(
            {
            "following_count": len(user_follow),
            "following_list": serializer.data
            }
        )   
        return JsonResponse(user_following_count_json, safe=False)
    
        
# 사용자가 팔로잉한 사람 숫자 보내기
@api_view(['GET'])
def follower_count(request, username):
    if request.method == 'GET':
        user_follow = get_list_or_404(Following, user_name=username)
        serializer = followingListSerializer(user_follow, many=True)
        user_following_count_json = []
        user_following_count_json.append(
            {
            "following_count": len(user_follow),
            "following_list": serializer.data
            }
        )   
        return JsonResponse(user_following_count_json, safe=False)

# 유저가 좋아하는 장르 출력, 유저가 좋아하는 장르 추가
@api_view(['GET', 'POST'])
def user_like_genre(request, username):
    if request.method == 'GET':
        print('asdasdasdsadsadsaasdasd')
        user_profile = get_list_or_404(UserLikeGenre, user_name=username)
        serializer = UserLikeGenreSerializer(user_profile)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserLikeGenreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# 유저가 좋아하는 영화 출력, 유저가 좋아하는 영화 추가
@api_view(['GET', 'POST'])
def user_like_movie(request, username):
    if request.method == 'GET':
        user_profile = get_list_or_404(UserLikeMovie, user_name=username)
        serializer = UserLikeMovieSerializer(user_profile)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserLikeMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 팔로우 여부 확인

# 언팔로우 = 팔로우 관계 삭제 구ㄹ현