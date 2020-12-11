
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from website.models import AssignTest
from website.decorators import candidate_required

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views import View

from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView

@method_decorator([login_required, candidate_required], name='dispatch')
class QuizList(ListView):
    model = AssignTest
    context_object_name = 'quizzes'
    template_name = 'website/quiz_list.html'
    
    def get_queryset(self):
        queryset = self.request.user.candidate.taken_quizzes
        return queryset

# def home(request):
#     if request.user.is_authenticated:
#         if request.user.is_evaluator:
#             return redirect('list')
#         elif request.user.is_candidate:
#             return redirect('list')
#         else:
#             return redirect('admin:index')
#     return render(request, 'website/home.html')

from website.forms import selectAssignTestForm
from quiz.models import Quiz 

from website.methods import create_quiz
from django.views.generic.edit import FormView 

class HomePageView(TemplateView):
    template_name = "website/home.html"

    


from django.urls import reverse
class TestView(FormView):
    model = AssignTest
    form_class = selectAssignTestForm
    template_name ='website/test.html'

    
    
    def form_valid(self, form):
        form.save()
        return super(TestView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')
