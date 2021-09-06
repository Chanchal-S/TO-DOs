# Generated by Django 2.1.15 on 2021-08-11 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_auto_20210811_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 15, 58, 868918)),
        ),
        migrations.AlterField(
            model_name='maps',
            name='country_svg',
            field=models.TextField(),
        ),
    ]