# Generated by Django 2.0.3 on 2018-03-26 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0007_fitness'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitness',
            name='calories',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fitness',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fitness',
            name='weight',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fitness',
            name='category',
            field=models.CharField(choices=[('Run', 'Run'), ('Cycle ride', 'Cycle ride'), ('Basketball', 'Basketball'), ('Yoga', 'Yoga'), ('Tennis', 'Tennis'), ('Football', 'Football'), ('Cricket', 'Cricket'), ('Badminton', 'Badminton'), ('CrossFit', 'CrossFit'), ('Weight Lifting', 'Weight Lifting'), ('Jump Rope', 'Jump Rope'), ('SWIMMING', 'Swimming')], db_column='Category', max_length=20),
        ),
    ]
