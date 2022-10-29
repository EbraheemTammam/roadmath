from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import Quiz, Score
from .serializers import QuizListSerializer, QuizDetailSerializer, ScoreSerializer
from .permissions import IsUserOrReadOnly

class QuizListView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer

class QuizDetailView(LoginRequiredMixin, generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

class ScoreViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    permission_classes = (IsUserOrReadOnly,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer