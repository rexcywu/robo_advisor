# Generated by Django 3.1.2 on 2020-10-12 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201012_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='volume',
            new_name='amount',
        ),
    ]