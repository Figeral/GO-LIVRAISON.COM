# Generated by Django 4.1 on 2023-07-22 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_alter_article_marque'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_article', to='stock.supplier'),
        ),
    ]
