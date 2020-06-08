# Generated by Django 2.2.5 on 2020-01-13 14:49

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200113_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 13, 14, 49, 32, 960431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]