
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, GenreListSerializer
from .models import Movie, Comment, Genre
from django.http import QueryDict, JsonResponse
from ast import literal_eval


# 영화 전체 정보 
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movie_list = get_list_or_404(Movie)
        serializer = MovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

# 영화 상세 정보 
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
# 전체 댓글 리스트
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
# 영화 각각에 단 댓글
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 영화 전체 정보 
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def all_genres(request):
    if request.method == 'GET':
        genre_list = get_list_or_404(Genre)
        serializer = GenreListSerializer(genre_list, many=True)
        return Response(serializer.data)
    
# 해당 영화의 장르 이름 보내주기
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def movie_genrename(request):
    if request.method == 'POST':
        genre_list = get_list_or_404(Genre) # 전체 장르 출력
        print(request.data['genre_id_list'])
        genre_name_list = []
        for i in genre_list:
             if i.id in request.data['genre_id_list']:
                print(i)
                genre_name_list.append(i.name)
        data = {
            'genre_name_list': genre_name_list
        }
        return JsonResponse(data)

        
        