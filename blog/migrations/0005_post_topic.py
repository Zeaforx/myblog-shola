# Generated by Django 4.2.7 on 2024-01-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="topic",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
