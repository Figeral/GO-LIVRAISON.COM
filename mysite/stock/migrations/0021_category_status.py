# Generated by Django 4.2.3 on 2023-08-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0020_category_slug_alter_article_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="status",
            field=models.CharField(
                choices=[("a", "Available"), ("ua", "Unavailable")],
                default="a",
                max_length=15,
            ),
        ),
    ]
