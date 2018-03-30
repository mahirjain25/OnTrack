from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomSignUp(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )



class ReminderForm(forms.ModelForm):
	class Meta:
		model = Reminder
		fields = ('text','due_date',)

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('isbn','name','author','date_issued','date_of_return','freq',)


class NumberOfSubjectsForm(forms.ModelForm):
	class Meta:
		model = NoOfSubjects
		fields = ('number',)

class SubjectsForm(forms.ModelForm):

	class Meta:
		model = Subjects
		fields = ('sub1','sub2','sub3','sub4','sub5','sub6','sub7',)
