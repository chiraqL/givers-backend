# Generated by Django 3.2.4 on 2021-07-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0010_remove_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
