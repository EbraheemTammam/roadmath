from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer
from .models import Article, Comment
from .permissions import IsAuthorOrReadOnly


class ArticleListView(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

class ArticleDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer