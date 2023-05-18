from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import FreeboardListSerializer, ReviewboardListSerializer
from .models import Freeboard, Reviewboard


# 영화 전체 정보 
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def freeboard_list(request):
    if request.method == 'GET':
        freeboard_list = get_list_or_404(Freeboard)
        serializer = FreeboardListSerializer(freeboard_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FreeboardListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE', 'PUT'])
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
        


def reviewboard_list(request):
    if request.method == 'GET':
        reviewboard_list = get_list_or_404(Reviewboard)
        serializer = ReviewboardListSerializer(reviewboard_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewboardListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET', 'DELETE', 'PUT'])
def reviewboard_detail(request, reviewboard_id):
    reviewboard_content = get_object_or_404(Reviewboard, id=reviewboard_id)

    if request.method == 'GET':
        serializer = FreeboardListSerializer(reviewboard_content)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        reviewboard_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeboardListSerializer(reviewboard_content, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        