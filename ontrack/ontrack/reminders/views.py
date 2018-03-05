from django.shortcuts import render
from .models import Reminder
from django.utils import timezone
from .forms import ReminderForm
from django.shortcuts import redirect

def reminder(request):
	reminders = Reminder.objects.filter(created_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'reminder.html',{'reminders': reminders})



def new_reminder(request):
	if request.method == "POST":
		form = ReminderForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.published_date = timezone.now()
			post.save()
			return redirect('reminders')
	else:
		form = ReminderForm()
	return render(request, 'new_form.html', {'form': form})

