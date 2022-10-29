from dataclasses import fields
from rest_framework import serializers

from .models import Quiz, Question, Answer, Score

from users.serializers import UserSerializer

class QuizIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('answer',)
        model = Answer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        fields = ('question', 'answers', 'true_answer',)
        model = Question

class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'sub_category', 'difficulty', )
        model = Quiz

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        fields = ('id', 'title', 'category', 'sub_category', 'difficulty', 'questions')
        model = Quiz

class QuizIdSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        model = Quiz

class ScoreSerializer(serializers.ModelSerializer):
    user = UserSerializer
    quiz = QuizIdSerializer
    class Meta:
        fields = ('id', 'user', 'quiz', 'score',)
        model = Score