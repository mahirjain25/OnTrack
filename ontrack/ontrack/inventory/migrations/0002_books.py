# Generated by Django 2.0.1 on 2018-03-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('isbn', models.IntegerField(db_column='ISBN', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Book Name', max_length=30)),
                ('author', models.CharField(db_column='Author Name', max_length=20)),
                ('date_issued', models.DateField(db_column='Date of Issue')),
                ('date_of_return', models.DateField(db_column='Date of Return')),
            ],
        ),
    ]
