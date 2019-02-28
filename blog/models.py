from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#class Category(models.Model):
	#title 				= 	models.CharField(max_length=200)

	#def __str__(self):
		#return self.title


class Question(models.Model):
	user 				=	models.ForeignKey(User, on_delete=models.CASCADE)
	#Category			=	models.ForeignKey(Category, on_delete=models.CASCADE)
	content				=	models.TextField()
	likes				=	models.ManyToManyField(User, related_name='likes', blank=True)
	created_date		=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse('blog:question-detail', kwargs={'pk': self.pk}) 
		#this will take us to the post detail for the specific question we have just added

class Answer(models.Model):
	user 				=	models.ForeignKey(User, on_delete=models.CASCADE)
	question 			=	models.ForeignKey(Question, on_delete=models.CASCADE)
	likes				=	models.ManyToManyField(User, related_name='answerlikes', blank=True)
	content				=	models.TextField()
	created_date		=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse('blog:blog-home',) 
		#this will take us to the post detail for the specific question we have just added