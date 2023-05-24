from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import FreeboardListSerializer, FreeboardcommentListSerializer
from .models import Freeboard, Freeboard_comment
from movies.models import Movie
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers


# 자유게시판 전체 조회
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def freeboard_list(request):
    if request.method == 'GET':
        freeboard_list = get_list_or_404(Freeboard)[::-1]
        serializer = FreeboardListSerializer(freeboard_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FreeboardListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def freeboard_detail(request, freeboard_id):
    freeboard_content = get_object_or_404(Freeboard, id=freeboard_id)

    if request.method == 'GET':
        serializer = FreeboardListSerializer(freeboard_content)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        print(freeboard_content)
        freeboard_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeboardListSerializer(freeboard_content, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        

# 자유게시판에서 검색할 때 사용
@api_view(['GET'])
def search_freeboard_list(request, search_keyword):
    print(search_keyword)
    related_freeboard_list = get_list_or_404(Freeboard)
    related_freeboards = []
    for ll in related_freeboard_list:
        if search_keyword in ll.title or search_keyword in ll.content or search_keyword in ll.Movie_title: # 리뷰 제목이나 내용이나 리뷰 무비 아이디에 있을 시
            related_freeboards.append(ll)
    related_freeboards_json = []        
    for k in related_freeboards:
        related_freeboards_json.append(
            {   
                "id": k.id,
                "title": k.title,
                "content" : k.content,
                "Movie_title" : k.Movie_title,
                "genre_name" : k.genre_name,
                "rating" : k.rating,
                "user_name" : k.user_name,
                "created_at" : k.created_at,
                "updated_at" : k.updated_at
            }
        )
    return JsonResponse(related_freeboards_json, safe=False)


# 쓴 글 조회 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_freeboard_list(request, user_name):
    if request.method == 'GET':
        freeboard_list = get_list_or_404(Freeboard, user_name=user_name)[::-1]
        serializer = FreeboardListSerializer(freeboard_list, many=True)
        return Response(serializer.data)


# 댓글 관련 함수들


# 해당 글의 댓글 전체 조회
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def freeboard_comment_list(request, article_id):
    if request.method == 'GET':
        freeboard_list = get_list_or_404(Freeboard_comment, freeboard_id=article_id)
        serializer = FreeboardcommentListSerializer(freeboard_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FreeboardcommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 특정 댓글 수정 삭제
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def freeboard_comment(request, comment_id):
    freeboard_comment_content = get_object_or_404(Freeboard_comment, id=comment_id)

    if request.method == 'GET':
        serializer = FreeboardcommentListSerializer(freeboard_comment_content)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        freeboard_comment_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeboardcommentListSerializer(freeboard_comment_content, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
# # 영화 디테일 페이지에서 제목으로 관련된 영화 리뷰 띄워줄 때 사용
# # 리뷰 게시판에서 영화 리뷰 검색할때도 사용
# @api_view(['GET'])
# def reviewboard_related_movie(request, related_movie_title):
#     movie_list = get_list_or_404(Movie)
#     reviewboard_review_list = get_list_or_404(Reviewboard)
#     related_reviews = []
#     related_movie_name = []
    
#     for i in movie_list:
#         if related_movie_title in i.title or related_movie_title in i.original_title:
#             related_movie_name.append(i.original_title)
#             related_movie_name.append(i.title)
#     print(related_movie_name)
            
#     for j in reviewboard_review_list:
#         for ll in related_movie_name:
#             print(ll)
#             if j.Movie_title in ll:
#                 related_reviews.append(j)
    
#     related_movie_json = []
#     for k in related_reviews:
#         related_movie_json.append(
#             {
#                 "Movie_title" : k.Movie_title,
#                 "genre_name" : k.genre_name,
#                 "title": k.title,
#                 "content" : k.content,
#             }
#         )
#     return JsonResponse(related_movie_json, safe=False)

# @api_view(['GET', 'POST'])
# def reviewboard_list(request):
#     if request.method == 'GET':
#         reviewboard_list = get_list_or_404(Reviewboard)
#         serializer = ReviewboardListSerializer(reviewboard_list, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ReviewboardListSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# @api_view(['GET', 'DELETE', 'PUT'])
# def reviewboard_detail(request, reviewboard_id):
#     reviewboard_content = get_object_or_404(Reviewboard, id=reviewboard_id)

#     if request.method == 'GET':
#         serializer = ReviewboardListSerializer(reviewboard_content)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         reviewboard_content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ReviewboardListSerializer(reviewboard_content, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def reviewboard_detail(request, comment_id):
#     reviewboard_content = get_object_or_404(Reviewboard, id=comment_id)

#     if request.method == 'GET':
#         serializer = ReviewboardListSerializer(reviewboard_content)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         reviewboard_content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ReviewboardListSerializer(reviewboard_content, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
