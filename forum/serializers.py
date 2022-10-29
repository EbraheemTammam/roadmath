from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

from .models import Comment, Article

class ArticleListSerializer(serializers.ModelSerializer):
    author = UserSerializer
    class Meta:
        model = Article
        fields = ('id', 'author', 'created_at', 'updated_at', 'title', 'body',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer
    article = ArticleListSerializer
    class Meta:
        model = Comment
        fields = ('id', 'author', 'article', 'created_at', 'updated_at', 'body',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer
    comments = CommentSerializer
    class Meta:
        model = Article
        fields = ('id', 'author', 'created_at', 'updated_at', 'title', 'body', 'comments',)