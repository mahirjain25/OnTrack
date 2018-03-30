from django.db import models

# Create your models here.


from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
import pickle

class Reminder(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	#title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	default=timezone.now)
	due_date = models.DateTimeField(
	blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['created_date']
		def __unicode__(self):
			return self.title


class Book(models.Model):
	isbn = models.IntegerField(primary_key=True,db_column='ISBN')
	name = models.CharField(db_column='Book Name', max_length=30)
	author = models.CharField(db_column = 'Author Name',max_length=20)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	date_issued = models.DateField(db_column='Date of Issue')
	date_of_return = models.DateField(db_column='Date of Return')
	freq = models.IntegerField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['date_of_return']
		def __unicode__(self):
			return self.name
    
   
class NoOfSubjects(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	number = models.IntegerField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.number, 

	class Meta:
		def __unicode__(self):
			return self.number



class Subjects(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	
	sub1 = models.CharField(max_length = 30)
	sub2 = models.CharField(blank = True ,max_length = 30, null = True)
	sub3 = models.CharField(blank = True,max_length = 30,null = True)
	sub4 = models.CharField(blank = True,max_length = 30,null = True)
	sub5 = models.CharField(blank = True,max_length = 30,null = True)
	sub6 = models.CharField(blank = True,max_length = 30,null = True)
	sub7 = models.CharField(blank = True,max_length = 30,null = True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.sub1, 

	class Meta:
		def __unicode__(self):
			return self.sub1

# class Timetable(models.Model):
# 	subjects = Subject.objects
# 	for i in subjects:
# 		if i.user.username ==User.username:
# 			break
	
class Timetable(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	Monday_Hour1 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour2 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour3 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour4 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour5 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour6 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour7 = models.CharField(blank = True ,max_length = 30, null = True)
	Monday_Hour8 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour1 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour2 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour3 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour4 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour5 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour6 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour7 = models.CharField(blank = True ,max_length = 30, null = True)
	Tuesday_Hour8 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour1 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour2 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour3 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour4 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour5 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour6 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour7 = models.CharField(blank = True ,max_length = 30, null = True)
	Wednesday_Hour8 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour1 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour2 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour3 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour4 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour5 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour6 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour7 = models.CharField(blank = True ,max_length = 30, null = True)
	Thursday_Hour8 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour1 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour2 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour3 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour4 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour5 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour6 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour7 = models.CharField(blank = True ,max_length = 30, null = True)
	Friday_Hour8 = models.CharField(blank = True ,max_length = 30, null = True)





