# Generated by Django 2.0.2 on 2018-03-05 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reminder',
            options={'ordering': ['created_date']},
        ),
        migrations.RenameField(
            model_name='reminder',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='slug',
        ),
        migrations.AddField(
            model_name='reminder',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reminder',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]