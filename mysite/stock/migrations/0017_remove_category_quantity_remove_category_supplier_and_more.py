# Generated by Django 4.1 on 2023-07-28 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='category',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='surname',
        ),
        migrations.AddField(
            model_name='category',
            name='added',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='category',
            field=models.ManyToManyField(related_name='category_supplier', to='stock.category'),
        ),
    ]
