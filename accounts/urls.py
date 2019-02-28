from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
	path('', views.index, name='index'),
	#path('question/<int:question_id>/', views.question_detail, name='question_detail'),
	#path('add_question', views.add_question, name='add_question'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]