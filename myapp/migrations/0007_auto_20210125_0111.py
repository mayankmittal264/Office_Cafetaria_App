# Generated by Django 3.1.5 on 2021-01-24 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210125_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 1, 11, 32, 699288), editable=False),
        ),
    ]
