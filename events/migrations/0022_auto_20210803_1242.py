# Generated by Django 2.1.15 on 2021-08-03 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_auto_20210803_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(12, 42, 22, 710845)),
        ),
    ]