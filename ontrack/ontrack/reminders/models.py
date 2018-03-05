from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Reminder(models.Model):
	#author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
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