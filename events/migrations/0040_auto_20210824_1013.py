# Generated by Django 2.1.15 on 2021-08-24 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0039_auto_20210823_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2021, 8, 24)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(10, 13, 39, 625453)),
        ),
    ]