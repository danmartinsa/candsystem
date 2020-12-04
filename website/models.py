from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.lookups import PostgresOperatorLookup
from django.utils.translation import ugettext_lazy as _
from quiz.models import Quiz

class User(AbstractUser):
    is_evaluator = models.BooleanField(default=False)
    is_interviwer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

# class Position(models.Model):
#     name =models.CharField(
#         verbose_name=_("Position Name"),
#         max_length=250, blank=True,
#         unique=True, null=True)

#     class Meta:
#         verbose_name = _("Position")
#         verbose_name_plural = _("Positions")
        

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE, unique=False)
    quiz_list  = models.ForeignKey(Quiz, on_delete=models.CASCADE, unique=False)

    class Meta:
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")
        



# Create your models here.
