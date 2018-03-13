# Generated by Django 2.0.1 on 2018-03-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('inventory', '0002_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothes',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
            preserve_default=False,
        ),
    ]
