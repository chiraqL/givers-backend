# Generated by Django 3.2.5 on 2021-08-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0023_auto_20210813_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='skills',
        ),
        migrations.AddField(
            model_name='user',
            name='skills_1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skills_2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skills_3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
