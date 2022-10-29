from operator import truth
from re import M
import uuid
from xml.parsers.expat import model
from django.db import models
from django.urls import reverse
from django.conf import settings


class Quiz(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz', args=[str(self.id)])

class Question(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    question = models.TextField()
    true_answer = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.question

class Answer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
    )
    answer = models.TextField()

    def __str__(self):
        return self.answer


class Score(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scores',
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='scores',
    )
    score = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' : ' + str(self.quiz)


