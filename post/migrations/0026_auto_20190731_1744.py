# Generated by Django 2.2.3 on 2019-07-31 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_auto_20190730_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 12, 14, 1, 149937, tzinfo=utc)),
        ),
    ]