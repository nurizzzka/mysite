from django import forms
from .models import DiaryMood


class MoodForm(forms.ModelForm):
	class Meta:
		model = DiaryMood
		fields = ('status', 'exersice', 'scale', 'date')
