# Generated by Django 4.2.7 on 2024-02-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0014_post_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.DeleteModel(
            name="like_post",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to="blog.category"
            ),
        ),
    ]
