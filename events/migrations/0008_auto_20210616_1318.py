# Generated by Django 2.1.15 on 2021-06-16 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210616_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 18, 27, 445621)),
        ),
    ]