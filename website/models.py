from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Quiz

class User(AbstractUser):
    is_evaluator = models.BooleanField(default=False)
    is_interviwer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quiz_list  = models.ForeignKey(Quiz, on_delete=models.CASCADE, unique=False)


# Create your models here.
