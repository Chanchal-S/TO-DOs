# Generated by Django 2.1.15 on 2021-06-16 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20210616_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 22, 5, 490579)),
        ),
    ]