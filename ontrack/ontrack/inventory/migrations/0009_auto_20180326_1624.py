# Generated by Django 2.0.3 on 2018-03-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20180326_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitness',
            name='weight',
            field=models.IntegerField(default=60),
        ),
    ]
