# Generated by Django 2.0.1 on 2018-03-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20180320_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.CharField(choices=[('Formal', 'Formal Wear'), ('Casual', 'Casual Wear'), ('Semi-Formal', 'Semi-Formal Wear'), ('Nightwear', 'Night Wear')], db_column='Category', max_length=20),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='colour',
            field=models.CharField(choices=[('White', 'White'), ('Red', 'Red'), ('Black', 'Black'), ('Blue', 'Blue'), ('Brown', 'Brown'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Green', 'Green'), ('Grey', 'Grey'), ('Pink', 'Pink'), ('Custom Colour', 'Custom Colour')], db_column='Colour', max_length=20),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='types',
            field=models.CharField(choices=[('Tee(s)', 'Tee(s)'), ('Pant(s)', 'Pants'), ('Jeans', 'Jeans'), ('Shirt(s)', 'Shirt(s)'), ('Shorts', 'Shorts)'), ('Undergarment(s)', 'Undergarment(s)'), ('Socks', 'Socks'), ('Ethnic Top(s)', 'Ethnic Top(s)'), ('Ethnic Bottom(s)', 'Ethnic Bottom(s)'), ('Top(s)', "Women's Top(s)"), ('Skirt(s)', 'Skirt(s)'), ('Leggings', 'Leggings/Skins'), ('Dress(es)', "Women's Dress(es)")], db_column='Type', max_length=20),
        ),
    ]
