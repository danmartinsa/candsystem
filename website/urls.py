# try:
#     from django.conf.urls import url
# except ImportError:
#     from django.urls import re_path as url

from django.urls import include, path
from .views import QuizList
from .views import HomeView
from django.shortcuts import render
from django.views import generic, static
from material.frontend import urls as frontend_urls
# from . import forms



urlpatterns = [  
    # path('',  include(frontend_urls)),
    path('list/', QuizList.as_view(), name='quiz_list'),
    path('', HomeView.as_view(), name='home'),
    
]

