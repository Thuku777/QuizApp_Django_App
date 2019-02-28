from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#from blog.models import Category

# Create your views here.
@login_required
def index(request):
	#atest_question_list 	= Question.objects.order_by('-created_date')[:5]
	#q_context 				= {'latest_question_list':	latest_question_list}
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account has been Updated and Picture Uploaded!')
			return HttpResponseRedirect(reverse('accounts:index'))
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		
	context = {
		'u_form'		: u_form,
		'p_form'		: p_form,
		#'categories'	: Category.objects.all()	
	}
	return render(request, 'accounts/index.html', context)

@login_required
def profile(request):
	return render(request, 'accounts/index.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#form1 = UserProfile(request.POST)
		if form.is_valid():
			#user = form.save(commit=False)
			form.save()
			#form1.user = user 
			#form1.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been Created! You can Login')
			return HttpResponseRedirect(reverse('accounts:login'))
	else:
		form = UserRegisterForm()	
	return render(request, 'accounts/register.html', {'form' : form})

#def login(request):
	#return render(request, 'accounts/login.html')

#def question_detail(request, question_id):
	#try:
		#question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
		#raise Http404("Question does not exist")
	#return render(request, 'accounts/question_detail.html', {'question': question})

#def add_question(request):
	#return render(request, 'accounts/add_question.html')
