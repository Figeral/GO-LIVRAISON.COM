# Generated by Django 4.1 on 2023-07-28 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_remove_category_quantity_remove_category_supplier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='supplier',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_article', to='stock.supplier'),
        ),
    ]
