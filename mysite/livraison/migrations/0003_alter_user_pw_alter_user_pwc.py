# Generated by Django 4.1 on 2023-07-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraison', '0002_rename_article_order_articleorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pw',
            field=models.CharField(max_length=50, verbose_name='mots de pass'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pwc',
            field=models.CharField(max_length=50, verbose_name='confirmation'),
        ),
    ]
