from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
	path('todo/new/', views.todo_new, name='todo_new'),
	path('todo/<int:pk>/edit/', TodoUpdate.as_view(), name='todo_edit'),
	path('todo/<int:pk>/delete/', Delete.as_view(), name='todo_delete'),
]	
