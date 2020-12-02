
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from .models import Candidate
from .decorators import candidate_required

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from django.views.generic import ListView

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

@method_decorator([login_required, candidate_required], name='dispatch')
class QuizList(ListView):
    model = Candidate
    context_object_name = 'quizzes'
    template_name = 'website/quiz_list.html'
    
    def get_queryset(self):
        queryset = self.request.user.candidate.taken_quizzes
        return queryset

def home(request):
    if request.user.is_authenticated:
        if request.user.is_evaluator:
            return redirect('list')
        elif request.user.is_candidate:
            return redirect('list')
        else:
            return redirect('admin:index')
    return render(request, 'website/home.html')