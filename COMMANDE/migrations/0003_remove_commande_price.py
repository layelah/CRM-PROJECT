# Generated by Django 4.1.7 on 2023-06-28 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('COMMANDE', '0002_commande_price_commande_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='price',
        ),
    ]
