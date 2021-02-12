from __future__ import unicode_literals
from six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from quiz.models import Question
from django.db import models


@python_2_unicode_compatible
class Essay_Question(Question):

    def check_if_correct(self, guess):
        return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")



@python_2_unicode_compatible
class Essay_Answer(models.Model):
    question = models.ForeignKey(Essay_Question, verbose_name=_("Question"), on_delete=models.CASCADE)

    content = models.TextField(
        blank=False,
        help_text=_("Enter the answer text that "
                    "you want displayed"),
        verbose_name=_("Content")
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
