# Generated by Django 5.1.5 on 2025-03-03 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullshop', '0007_alter_product_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='fullshop.category'),
        ),
    ]
