# try:
#     from django.conf.urls import url
# except ImportError:
#     from django.urls import re_path as url

from django.urls import include, path
from .views import QuizList
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('list/', QuizList.as_view(), name='quiz_list'),
]