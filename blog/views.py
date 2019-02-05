from django.shortcuts import render
from .models import *


def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def student_list(request):
	students = Students.objects.all()
	return render(request, 'blog/post_list.html')