from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ArticleListView, ArticleDetailView, CommentViewSet


router = SimpleRouter()
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<uuid:pk>/', ArticleDetailView.as_view()),
] + router.urls