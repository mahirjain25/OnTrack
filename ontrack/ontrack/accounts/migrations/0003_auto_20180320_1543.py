# Generated by Django 2.0.1 on 2018-03-20 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='author',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]