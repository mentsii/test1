# Generated by Django 5.1.5 on 2025-03-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-time_create'], name='fullshop_pr_time_cr_bd97aa_idx'),
        ),
    ]
