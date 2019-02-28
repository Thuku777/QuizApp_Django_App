from django.urls import path
from django.conf.urls import url
from .views import (
	QuestionListView, 
	QuestionDetailView, 
	QuestionCreateView,
	QuestionUpdateView,
	QuestionDeleteView,
	AnswerCreateView,
	UserQuestionListView,
	#QuestionAnswerListView,
)
from . import views

app_name = 'blog'
urlpatterns = [
	path('',QuestionListView.as_view(), name='blog-home'),
	path('user/<str:username>/',UserQuestionListView.as_view(), name='user-question'),
	path('question/<int:pk>/',QuestionDetailView.as_view(), name='question-detail'),	
	path('question/<int:pk>/',views.question_detail, name='question-answer'),
	path('question/new/',QuestionCreateView.as_view(), name='question-create'),
	path('answer/new/<int:pk>/',AnswerCreateView.as_view(), name='answer-create'),
	path('question/<int:pk>/update/',QuestionUpdateView.as_view(), name='question-update'),
	path('question/<int:pk>/delete/',QuestionDeleteView.as_view(), name='question-delete'),	
	path('about/', views.about, name='blog-about'),
]