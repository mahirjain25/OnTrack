from django.contrib.auth.models import User 
from django.test import TestCase
from .forms import AddFitnessForm
from .models import Fitness
import datetime
import random

class FitnessTest(TestCase):
    
    #Test to make sure a normal fitness activity is valid
    def test_init(self):
        user = User.objects.create_user('sadadafad')
        duration = random.randint(30,60)
        weight = random.randint(50,100)
        form_data = {'category': 'Run' ,'duration':duration, 'weight':weight}
        form = AddFitnessForm(data = form_data)
        self.assertTrue(form.is_valid())
    #Making sure that reminders aren't set for dates in the past 
    def test_negative_duration(self):
        date = datetime.date.today() - datetime.timedelta(days =1)
        duration = random.randint(30,60)
        form_data = {'category': 'Run' ,'duration':duration, 'weight':-1}
        form = AddFitnessForm(data = form_data)
        self.assertFalse(form.is_valid())