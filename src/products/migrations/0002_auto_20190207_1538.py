# Generated by Django 2.0.7 on 2019-02-07 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='proce',
            new_name='price',
        ),
    ]
