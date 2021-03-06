# Generated by Django 2.0.7 on 2018-08-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0003_auto_20180807_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoapp',
            options={'ordering': ['-time_added']},
        ),
        migrations.AddField(
            model_name='todoapp',
            name='created',
            field=models.DateTimeField(default='2018-08-13'),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='time_added',
            field=models.DateTimeField(default='2018-08-13'),
        ),
    ]
