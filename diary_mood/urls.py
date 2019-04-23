from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', MoodList.as_view(), name = 'mood_list'),
	path('add/', MoodCreate.as_view(), name = 'mood_add'),
	path('detail/<int:pk>', MoodDetail.as_view(), name = 'mood_detail'),
	path('edit/<int:pk>', MoodUpdate.as_view(), name = 'mood_edit'),
	path('delete/<int:pk>', MoodDelete.as_view(), name = 'mood_delete'),
	]