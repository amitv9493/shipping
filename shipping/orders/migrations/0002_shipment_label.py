# Generated by Django 4.2 on 2023-04-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='label',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Label'),
        ),
    ]
