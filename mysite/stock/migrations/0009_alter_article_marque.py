# Generated by Django 4.1 on 2023-07-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_remove_article_fournisseur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='marque',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
