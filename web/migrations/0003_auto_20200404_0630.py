# Generated by Django 3.0.2 on 2020-04-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_incom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='incom',
            old_name='data',
            new_name='date',
        ),
    ]
