from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'id title body is_published'.split()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id body'.split()