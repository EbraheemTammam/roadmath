from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    QuizListView, QuizDetailView, ScoreViewSet
)

router = SimpleRouter()
router.register('scores', ScoreViewSet, basename = 'scores')

urlpatterns = [
    path('quizs/', QuizListView.as_view()),
    path('quizs/<uuid:pk>/', QuizDetailView.as_view()),
] + router.urls