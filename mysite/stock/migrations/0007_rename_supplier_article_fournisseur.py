# Generated by Django 4.1 on 2023-07-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_article_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='supplier',
            new_name='fournisseur',
        ),
    ]
