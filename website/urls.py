# try:
#     from django.conf.urls import url
# except ImportError:
#     from django.urls import re_path as url

from django.urls import include, path
from .views import QuizList
from .views import HomePageView, TestView, takeTest
from django.shortcuts import render
from django.views import generic, static
from material.frontend import urls as frontend_urls
# from . import forms



urlpatterns = [  
    # path('',  include(frontend_urls)),
    path('list/<str:quiz_url>', takeTest, name='taskeTest'),
    path('', HomePageView.as_view(), name='home'),
    path('assignquiz/', TestView.as_view(), name='assignquiz'),
    
]

