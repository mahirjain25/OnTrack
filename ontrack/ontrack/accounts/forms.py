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

	def clean_reminder_data(self):
		data = self.cleaned_data['due_date']

		if data < datetime.date.today():
			raise ValidationError(('Invalid date - reminder in the past'))

		return data

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('name','author','date_issued','date_of_return',)
		#Making sure return date cannot be earlier than date of issue
		def clean_book_data(self):
			issued = self.cleaned_data['date_issued']
			ret = self.cleaned_date['date_of_return']
			if(ret>issued):
				raise ValidationError(('Date of return is before the date of issue'))
			return ret #just in case	

class NumberOfSubjectsForm(forms.ModelForm):
	class Meta:
		model = NoOfSubjects
		fields = ('number',)

class SubjectsForm(forms.ModelForm):

	class Meta:
		model = Subjects
		fields = ('sub1','sub2','sub3','sub4','sub5','sub6','sub7',)


class TimetableForm(forms.ModelForm):

	class Meta:
		model = Timetable
		fields = ('Monday_Hour1','Monday_Hour2','Monday_Hour3','Monday_Hour4','Monday_Hour5','Monday_Hour6','Monday_Hour7','Monday_Hour8','Tuesday_Hour1','Tuesday_Hour2','Tuesday_Hour3','Tuesday_Hour4','Tuesday_Hour5','Tuesday_Hour6','Tuesday_Hour7','Tuesday_Hour8','Wednesday_Hour1','Wednesday_Hour2','Wednesday_Hour3','Wednesday_Hour4','Wednesday_Hour5','Wednesday_Hour6','Wednesday_Hour7','Wednesday_Hour8','Thursday_Hour1','Thursday_Hour2','Thursday_Hour3','Thursday_Hour4','Thursday_Hour5','Thursday_Hour6','Thursday_Hour7','Thursday_Hour8','Friday_Hour1','Friday_Hour1','Friday_Hour2','Friday_Hour3','Friday_Hour4','Friday_Hour5','Friday_Hour6','Friday_Hour7','Friday_Hour8',)

