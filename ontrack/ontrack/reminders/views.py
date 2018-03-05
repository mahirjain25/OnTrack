from django.shortcuts import render
from .models import Reminder
from django.utils import timezone

def reminder(request):
	reminders = Reminder.objects.filter(created_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'reminder.html',{'reminders': reminders})



