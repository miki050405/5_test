from rest_framework.response import Response
from rest_framework import status
from .models import Post,Comment
from .serializers import (
    PostSerializer, PostValidateSerializer,
    CommentSerializer, CommentValidateSerializer
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class PostListCreateApiView(ListCreateAPIView):
    queryset = Post.objects.filter(is_published = True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return PostValidateSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise ValidationError('User is not authenticated')
        serializer.save(author=self.request.user)

class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return PostValidateSerializer
        return self.serializer_class
    
    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    
class CommentListCreateApiView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id=self.kwargs['id']
        return Comment.objects.filter(post_id=post_id, is_approved = True)
    
    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return CommentValidateSerializer
        return self.serializer_class
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user,post_id=self.kwargs['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
