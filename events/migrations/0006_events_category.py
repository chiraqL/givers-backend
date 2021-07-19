# Generated by Django 3.2.4 on 2021-07-15 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('events', '0005_alter_events_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='category',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='category.eventcategory'),
            preserve_default=False,
        ),
    ]
