# Generated by Django 4.2 on 2023-04-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_shipment_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='label',
        ),
        migrations.AddField(
            model_name='order',
            name='label',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Label'),
        ),
    ]
