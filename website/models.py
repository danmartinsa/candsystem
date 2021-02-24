from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.lookups import PostgresOperatorLookup
from django.utils.translation import ugettext_lazy as _
from quiz.models import Quiz, Sitting
from datetime import datetime

class User(AbstractUser):
    is_evaluator = models.BooleanField(default=False)
    is_interviwer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)

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
    

class Rules(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, unique=False, related_name="candidate")

    n_basic_obj = models.IntegerField(verbose_name=_("Objective Basic Questions"))
    n_intermediate_obj = models.IntegerField(verbose_name=_("Objective Intermediate Questions"))
    n_advanced_obj = models.IntegerField(verbose_name=_("Objective Advanced Questions"))

    n_basic_subj = models.IntegerField(verbose_name=_("Subjective Basic Questions"))
    n_intermediate_subj = models.IntegerField(verbose_name=_("Subjective Intermediate Questions"))
    n_advanced_subj = models.IntegerField(verbose_name=_("Subjective Advanced Questions"))

    mark_basic_obj = models.IntegerField(verbose_name=_("Mark Basic Obj"))
    mark_intermediate_obj = models.IntegerField(verbose_name=_("Mark Intermediate Obj"))
    mark_advanced_obj = models.IntegerField(verbose_name=_("Mark Advanced Obj"))

    mark_basic_subj = models.IntegerField(verbose_name=_("Mark Basic Subj"))
    mark_intermediate_subj = models.IntegerField(verbose_name=_("Mark Intermediate Subj"))
    mark_advanced_subj = models.IntegerField(verbose_name=_("Mark Advanced Subj"))

    class Meta:
        verbose_name = _("Rule")
        verbose_name_plural = _("Rules")

    def __str__(self):
        return self.role.name


class AssignTest(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="candidate")
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="requestor")
    evaluator_1  = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, related_name="evaluator_1")
    evaluator_2 = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, related_name="evaluator_2")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, unique=False)
    quiz  = models.ForeignKey(Quiz, on_delete=models.CASCADE, unique=False)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE, unique=False)
    date_created=models.DateTimeField(default=datetime.now)

    @property
    def language(self):
        if self.quiz is None:
            return None

        language = self.quiz.category
        return language
    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")

    def __str__(self):
        name = self.candidate.username, self.quiz.category, self.role, self.quiz.title
        return str(name)
        

class Evaluation(models.Model):
    sitting =  models.ForeignKey(Sitting, on_delete=models.CASCADE, unique=False, null=True, related_name="sitting")
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, related_name="evaluator")
    score =  models.IntegerField(verbose_name=_("Objective Basic Questions"))
    comments = models.TextField(blank=False, verbose_name=_("Comment"))
    


# Create your models here.
