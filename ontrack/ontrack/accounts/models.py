from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(db_column='Username',max_length=12)
	uid = models.AutoField(primary_key = True)
	password = models.CharField(max_length = 15)
	
