# Generated by Django 5.1.5 on 2025-03-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullshop', '0002_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
