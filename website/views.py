
from django import urls
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from django.utils.translation import LANGUAGE_SESSION_KEY
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

from quiz.models import Category, Quiz
from website.forms import selectAssignTestForm
from website.models import User, Role, AssignTest

@method_decorator([login_required, candidate_required], name='dispatch')
class QuizList(ListView):
    model = AssignTest
    context_object_name = 'quizzes'
    template_name = 'website/quiz_list.html'
    
    def get_queryset(self):
        candidate = self.request.user
        quiz_list = AssignTest.objects.filter(candidate=candidate)
        queryset = Quiz.objects.filter(PK__in=quiz_list)
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




from website.methods import create_quiz
from django.views.generic.edit import CreateView, FormView 

class HomePageView(TemplateView):
    template_name = "website/home.html"

    

from django.urls import reverse
@method_decorator([login_required], name='dispatch')
class TestView(FormView):
    form_class = selectAssignTestForm
    template_name ='website/test.html'
        
    def get_context_data(self, **kwargs):
     # Call the base implementation first to get a context
        c = super(TestView, self).get_context_data(**kwargs)
        user = self.request.user
        return c
    
    def form_valid(self, form, **kwargs):
        email = form.cleaned_data['candidate']  # <--- Add this line to get email value
        category = Category.objects.get(id=form.cleaned_data['category'])
        role = Role.objects.get(id=form.cleaned_data['role'])
        quiz = create_quiz(plang=category, position=role, user_email=email, interviewer=self.request.user)
        

        if quiz is not None:      
            return super(TestView, self).form_valid(form)
        else:
            return None


    def get_success_url(self):
        return reverse('home')

from quiz.models import Quiz, Question, Sitting
from quiz.forms import QuestionForm, EssayForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.forms.models import inlineformset_factory
from django.forms import inlineformset_factory


def takeTest(request, quiz_url):
    if request.user.is_authenticated:
        user = request.user
    quiz = Quiz.objects.get(url=quiz_url)
    

    


    


