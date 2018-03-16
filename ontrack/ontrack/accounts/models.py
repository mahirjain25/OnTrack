from django.db import models

# Create your models here.


from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

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
    
   
