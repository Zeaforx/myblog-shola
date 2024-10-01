# Generated by Django 4.2.7 on 2024-03-07 21:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0015_remove_post_category_delete_like_post_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ManyToManyField(
                blank=True, related_name="cats", to="blog.category"
            ),
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message_body", models.TextField()),
                ("created", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "mpost",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.post",
                    ),
                ),
                (
                    "muser",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.profile",
                    ),
                ),
            ],
        ),
    ]
