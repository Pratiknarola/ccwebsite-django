# Generated by Django 2.2.3 on 2019-08-16 14:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20190814_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 16, 14, 17, 55, 554412, tzinfo=utc)),
        ),
    ]
