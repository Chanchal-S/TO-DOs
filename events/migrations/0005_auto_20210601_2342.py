# Generated by Django 2.1.15 on 2021-06-01 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210527_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2021, 6, 1)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(23, 42, 51, 974270)),
        ),
    ]
