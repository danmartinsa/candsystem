# try:
#     from django.conf.urls import url
# except ImportError:
#     from django.urls import re_path as url

from django.conf.urls import url
from django.urls import include, path
from .views import QuizList
from .views import HomePageView, TestView,Taketest, takeTest, SuccessView, success, home, insights
from django.shortcuts import render
from django.views import generic, static
from material.frontend import urls as frontend_urls
from django.contrib.auth import views as auth_views
# from . import forms

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

urlpatterns = [  
    path('',  include(frontend_urls)),
    path('list/<str:quiz_url>', Taketest, name='taskeTest'),
    path('', home, name='home'),
    path('insights/', insights, name='insights'),
    # path('', HomePageView.as_view(), name='home'),
    # path('success/', SuccessView.as_view(), name='success'),
    path('assignquiz/', TestView.as_view(), name='assignquiz'),   
]
urlpatterns = urlpatterns + [
    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=Taketest.as_view(),
        name='quiz_question'),
    url(r'^success/$',success,name='success'),
    
]

# urlpatterns = [
#     url(r'login/', auth_views.login, name='login'),
#     url(r'logout/', auth_views.logout, name='logout'),
#     url(r'admin/', admin.site.urls),
# ]

