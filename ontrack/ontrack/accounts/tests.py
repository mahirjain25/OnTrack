from django.contrib.auth.models import User 
from django.test import TestCase
from .forms import ReminderForm, BookForm
from .models import Reminder, Book
import datetime

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class ReminderTest(TestCase):
    
    #Test to make sure a normal reminder is valid
    def test_init(self):
        user = User.objects.create_user('sadadafad')
        date = datetime.date.today() + datetime.timedelta(days =1)
        form_data = {'text': 'abcd' ,'due_date':date}
        form = ReminderForm(data = form_data)
        self.assertTrue(form.is_valid())
    #Making sure that reminders aren't set for dates in the past 
    def test_past_reminder_date(self):
        date = datetime.date.today() - datetime.timedelta(days =1)
        form_data = {'due_date' : date}
        form = ReminderForm(data = form_data)
        self.assertFalse(form.is_valid())

class BookTest(TestCase):
    
    #Test to make sure an expected book should be valid
    def test_init(self):
        user = User.objects.create_user('hehe')
        self.book = Book.objects.create(user = user, isbn = 123,name = "Animal Farm", author = "George Orwell", date_issued = "2018-03-02", date_of_return = "2018-03-16", freq =2)
        issue = datetime.date.today()
        ret = datetime.date.today() + datetime.timedelta(days =1)
        form_data = {"user":user, "isbn":1234, "name" : "Animal Farm", "author": "George Orwell", "date_issued":issue, "date_of_return":ret, "freq":2}

        form = BookForm(form_data)
        self.assertTrue(form.is_valid())
        
    #Test to make sure renewal date cannot be before date of issue
    def test_renewal_before_issue(self):
        renew = datetime.date.today() - datetime.timedelta(days =1)
        issue  = datetime.date.today()
        form_data = {'date_issued':issue,'date_of_return' : renew}
        form = BookForm(data = form_data)
        self.assertFalse(form.is_valid())
    #Maybe test that you can't enter a char in isbn etc? (datetype errors)