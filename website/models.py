from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.lookups import PostgresOperatorLookup
from django.utils.translation import ugettext_lazy as _
from quiz.models import Quiz, Sitting

class User(AbstractUser):
    is_evaluator = models.BooleanField(default=False)
    is_interviwer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class Role(models.Model):
    name = models.CharField(
        verbose_name=_("Role Name"),
        max_length=250, blank=True,
        unique=True, null=True)

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

    def __str__(self):
        return self.name
    
        

class AssignTest(models.Model):
    candidate = models.OneToOneField(User, on_delete=models.CASCADE, unique=False, related_name="candidate")
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="requestor")
    evaluator_1  = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, related_name="evaluator_1")
    evaluator_2 = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, related_name="evaluator_2")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, unique=False)
    quiz  = models.ForeignKey(Quiz, on_delete=models.CASCADE, unique=False)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE, unique=False)


    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
        



# Create your models here.
