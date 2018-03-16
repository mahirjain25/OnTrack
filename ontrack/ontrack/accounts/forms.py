from django import forms

from .models import Reminder, Book


class ReminderForm(forms.ModelForm):
	class Meta:
		model = Reminder
		fields = ('text','due_date',)

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('isbn','name','author','date_issued','date_of_return','freq',)