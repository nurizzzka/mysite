from django.shortcuts import render
from .models import *


def index(request):
	todo_list = TodoList.objects.all()
	context = {'todo_list' : todo_list}
	return render(request, 'todo/index.html', context)


