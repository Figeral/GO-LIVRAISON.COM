# Generated by Django 4.1 on 2023-07-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_article_image_alter_article_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='size',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
