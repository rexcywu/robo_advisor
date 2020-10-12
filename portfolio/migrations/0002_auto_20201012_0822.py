# Generated by Django 3.1.2 on 2020-10-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='price',
            new_name='buying_price',
        ),
        migrations.AddField(
            model_name='stocks',
            name='today_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stocks',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]