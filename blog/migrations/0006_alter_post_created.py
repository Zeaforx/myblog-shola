# Generated by Django 4.2.7 on 2024-01-27 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
