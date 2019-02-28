from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Answer, Answer


# Create your views here.

def home(request):
	#context = {
	#	'categories' 	:	Category.objects.all(),
	#}
	return render(request,'blog/home.html')

def question_detail(request):
	context = {
		'answers'	:	Answers.objects.all(),
	}
	return render(request, 'blog:quetion-answer', context)

class QuestionListView(LoginRequiredMixin, ListView):
	model = Question
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'questions'
	ordering = ['-created_date']
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(QuestionListView, self).get_context_data(**kwargs)
		#context['categories'] = Category.objects.all()
		return context

class UserQuestionListView(LoginRequiredMixin, ListView):
	model = Question
	template_name = 'blog/user_question.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'questions'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Question.objects.filter(user=user).order_by('-created_date')


class QuestionDetailView(LoginRequiredMixin, DetailView):
	model = Question

	def get_context_data(self, **kwargs):
		context = super(QuestionDetailView, self).get_context_data(**kwargs)
		context['answers'] = Answer.objects.filter(question=self.kwargs.get('pk'))
		#context['categories'] = Category.objects.filter(question=self.kwargs.get('pk'))
		return context

class QuestionCreateView(LoginRequiredMixin, CreateView):
	model 		=	Question
	fields 		=	['content'] 

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class AnswerCreateView(LoginRequiredMixin, CreateView):
	model 		=	Answer
	fields 		=	['content']

	def dispatch(self, *args, **kwargs):
		self.question = get_object_or_404(Question, pk=self.kwargs['pk'])
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.question = self.question
		print(self.kwargs['pk'])
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AnswerCreateView, self).get_context_data(**kwargs)
		context['questions'] = Question.objects.filter(pk=self.kwargs.get('pk'))
		return context



class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
 	model 		=	Question
 	fields 		=	['content']

 	def form_valid(self, form):
 		form.instance.user = self.request.user
 		return super().form_valid(form)

 	def test_func(self):
 		question = self.get_object()
 		if self.request.user == question.user:
 			return True
 		return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Question
	success_url = '/'

	def test_func(self):
 		question = self.get_object()
 		if self.request.user == question.user:
 			return True
 		return False

def about(request):
	return render(request,'blog/home.html', {'title': 'About'})