from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add-ques/', views.add_questions, name='ques'),
]
