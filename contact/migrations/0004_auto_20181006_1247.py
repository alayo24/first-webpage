# Generated by Django 2.0.7 on 2018-10-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20181006_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_added',
            field=models.DateField(),
        ),
    ]
