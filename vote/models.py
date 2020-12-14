from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionModel(models.Model):
    question_title = models.CharField(max_length=200)
    published = models.DateTimeField('date published')
    voted = models.ManyToManyField(
        User, default=None, blank=True, related_name='voted')

    def __str__(self) -> str:
        return self.question_title


class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    choice_title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_title
