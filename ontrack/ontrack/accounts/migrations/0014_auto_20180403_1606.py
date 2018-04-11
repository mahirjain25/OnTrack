# Generated by Django 2.0.1 on 2018-04-03 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180403_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(db_column='ISBN', max_length=13, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(13)]),
        ),
    ]