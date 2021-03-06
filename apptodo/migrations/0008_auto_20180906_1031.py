# Generated by Django 2.0.7 on 2018-09-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0007_auto_20180906_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoapp',
            options={'ordering': ['-time_added']},
        ),
        migrations.AddField(
            model_name='todoapp',
            name='due_date',
            field=models.DateField(default='2018-09-06'),
        ),
        migrations.AddField(
            model_name='todoapp',
            name='name',
            field=models.CharField(default='general', max_length=30),
        ),
        migrations.AddField(
            model_name='todoapp',
            name='time_added',
            field=models.DateTimeField(default='2018-09-06'),
        ),
    ]
