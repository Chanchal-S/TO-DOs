# Generated by Django 2.1.15 on 2021-08-25 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_auto_20210824_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2021, 8, 25)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(11, 59, 13, 808861)),
        ),
    ]
