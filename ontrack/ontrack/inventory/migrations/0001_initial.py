# Generated by Django 2.0.1 on 2018-03-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(db_column='Qty')),
                ('types', models.CharField(choices=[('TEE', 'Tees'), ('PNT', 'Pants'), ('JNS', 'Jeans'), ('SHR', 'Shirts'), ('SHT', 'Shorts'), ('UNG', 'Undergarments'), ('SCK', 'Socks'), ('ETT', 'Ethnic Top'), ('ETB', 'Ethnic Bottom'), ('TOP', "Women's Top"), ('SKT', 'Skirt'), ('LEG', 'Leggings/Skins'), ('DRS', "Women's Dress")], db_column='Type', max_length=3)),
                ('category', models.CharField(choices=[('FL', 'Formal Wear'), ('CL', 'Casual Wear'), ('SF', 'Semi-Formal Wear'), ('NW', 'Night Wear')], db_column='Category', max_length=2)),
                ('colour', models.CharField(choices=[('WT', 'White'), ('RD', 'Red'), ('BL', 'Black'), ('BE', 'Blue'), ('BR', 'Brown'), ('YL', 'Yellow'), ('OR', 'Orange'), ('PL', 'Purple'), ('GR', 'Green'), ('GY', 'Grey'), ('PK', 'Pink'), ('OT', 'Other')], db_column='Colour', max_length=2)),
                ('tag', models.TextField(max_length=20)),
            ],
        ),
    ]
