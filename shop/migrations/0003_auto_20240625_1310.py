# Generated by Django 2.2 on 2024-06-25 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
