
from datetime import datetime, date
from itertools import count
from typing import Coroutine
from django import urls
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from django.utils.translation import LANGUAGE_SESSION_KEY, to_language
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
from website.forms import selectAssignTestForm, QuestionForm
from website.models import User, Role, AssignTest

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


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


from website.models import AssignTest

def home(request):
    if request.user.is_authenticated:
      
        data = AssignTest.objects.filter(requestor = request.user)
       
        ntotal = 0
        ncomplete = 0
        for i in data:
            print(i.sitting.complete)
            if i.sitting.complete:
                ntotal = ntotal + 1
                ncomplete = ncomplete + 1
            else :
                ntotal = ntotal + 1

        
        return render(request, 'website/home.html', {'data': data, 'ntotal':ntotal, 'ncomplete':ncomplete} )
    return render(request, 'registration/login.html')

def insights(request):
    if request.user.is_authenticated:
      
        data = AssignTest.objects.all()
       
        ntotal = 0
        ncomplete = 0
        for i in data:
            print(i.sitting.complete)
            if i.sitting.complete:
                ntotal = ntotal + 1
                ncomplete = ncomplete + 1
            else :
                ntotal = ntotal + 1

        return render(request, 'website/insights.html', {'data': data, 'ntotal':ntotal, 'ncomplete':ncomplete} )
    return render(request, 'registration/login.html')


def success(request):
    if request.user.is_authenticated:
        if request.user.is_candidate:
            return render(request, 'website/success.html' )
        else: 
            data = AssignTest.objects.filter(requestor = request.user)
            last = 0
            for i in data: 
              
                last = i
            return render(request, 'website/success.html', {'data': last } )
       
    return render(request, 'website/home.html')

# def success(request):
#     if request.user.is_authenticated:
#         print(request.user.is_evaluator, request.user.is_candidate)
#         data = AssignTest.objects.filter(requestor = request.user)
#         last = 0
#         for i in data: 
#             print(i)
#             last = i
#         return render(request, 'website/success.html', {'data': last } )
        
#     return render(request, 'website/home.html')





from website.methods import create_quiz
from django.views.generic.edit import CreateView, FormView 
from website.models import AssignTest
from django.views import generic

# @method_decorator([login_required], name='dispatch')
class HomePageView(TemplateView):
    template_name = "website/home.html"
    

class SuccessView(TemplateView):
  
    template_name = "website/success.html"

   
    

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
        quiz_candidate = User.objects.get(username=email)

        if quiz is not None:

            #Candidate Email message
            email_subject= "Evalueserve Skill Questionnaire"
            email_body = """
                Quiz: http://localhost:8000/%s/take  
                Access ID: %s
                Access Key: %s 
            """ % (quiz.url,  email, "evs123")
            send_mail(
                email_subject, email_body,
                "<danilo.m.a@gmail.com>", [email, "danilo.m.a@gmail.com"])

            
            #Requestor email message
            requestor_email = self.request.user.username
            requestor_email_subject = "Questionnaire has been sent out to %s" % (email)
            requestor_body = """
            On date %s Questionnaire has been sent out to %s.
                Role: %s
                Skill: %s 
            """ % (str(date.today()), email, role, quiz.category)
            send_mail(
                    requestor_email_subject, requestor_body,
                    "<danilo.m.a@gmail.com>", [requestor_email, "danilo.m.a@gmail.com"])
            return super(TestView, self).form_valid(form)
        else:
            return None


    def get_success_url(self):
        return reverse('success')

from quiz.models import Quiz, Question, Sitting
# from quiz.forms import QuestionForm, EssayForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.forms.models import inlineformset_factory
from django.forms import inlineformset_factory


def takeTest(request, quiz_url):
    if request.user.is_authenticated:
        user = request.user
    quiz = Quiz.objects.get(url=quiz_url)
     
    


from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin


@method_decorator([login_required], name='dispatch')
class Taketest(FormView):
    form_class = QuestionForm
    template_name ='website/attempt.html'

    def dispatch(self, request, *args, **kwargs):
        
        self.quiz = get_object_or_404(Quiz, url=self.kwargs['quiz_name'])

        try:
            self.logged_in_user = self.request.user.is_authenticated()
        except TypeError:
            self.logged_in_user = self.request.user.is_authenticated

        

        if self.logged_in_user:
            self.sitting = Sitting.objects.get(user_id=self.request.user.id, quiz_id=self.quiz.id)
            self.test = AssignTest.objects.get(sitting=self.sitting.id)

           
        return super(Taketest, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Taketest, self).get_context_data(**kwargs)
        context["quiz"] = self.quiz
        context["test"] = self.test
        context["sitting"] = self.sitting
        
        
        return context
    
    
    def get_form_kwargs(self):
        kwargs = super(Taketest, self).get_form_kwargs()

        return dict(kwargs, quiz=self.quiz)
    
    def form_valid(self, form, **kwargs):
        question_list = self.quiz.get_questions()
        score = 0
        total_weight = 0
        user_answers = []
        
        for question in question_list:
            field_name = str(question.id) + "answerset"
            guess = form.cleaned_data[field_name]
            print(guess)

            flag_blank = False
            
            if guess != '':
                is_correct = question.check_if_correct(guess)
                user_answers.append((question.content, is_correct))
            else :
                flag_blank = True
                is_correct = False

            total_weight = total_weight + question.weight
            if is_correct == True:
                score= score + (1 * question.weight)
        
        
        self.sitting.current_score = score
        self.sitting.pct_score = (score/total_weight) * 100
        self.sitting.user_answers = user_answers
        self.sitting.mark_quiz_complete()
        self.sitting.save()
        self.test = AssignTest.objects.get(sitting=self.sitting.id)
        print("score", self.sitting.current_score)

        email = self.test.candidate
        email_subject = "Questionnaire has been completed. Check Score." 
        email_body = """
        On date %s Questionnaire completed by %s.
            Role: %s
            Skill: %s
            Score: %s 
        """ % (str(date.today()), email, self.test.role, self.sitting.quiz.category,  "{}{}".format(self.sitting.pct_score,"%"))
        send_mail(
                email_subject, email_body,
                "<danilo.m.a@gmail.com>", [self.test.requestor, "danilo.m.a@gmail.com"])

        return super(Taketest, self).form_valid(form)

    def get_success_url(self):
        return reverse('success')

