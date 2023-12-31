# Generated by Django 4.1 on 2023-07-26 13:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0015_alter_article_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'costumer',
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('complete', models.BooleanField(default=False)),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_order', to='livraison.customer')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pw', models.CharField(max_length=50)),
                ('pwc', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='shippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=50)),
                ('quater', models.CharField(max_length=50)),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order_sa', to='livraison.order')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_sa', to='livraison.customer')),
            ],
            options={
                'verbose_name': 'shippingAddress',
                'verbose_name_plural': 'shippingAddresses',
            },
        ),
        migrations.CreateModel(
            name='Article_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_articleorder', to='stock.article')),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_articleorder', to='livraison.order')),
            ],
            options={
                'verbose_name': 'Article_Order',
                'verbose_name_plural': 'Article_Orders',
            },
        ),
    ]
