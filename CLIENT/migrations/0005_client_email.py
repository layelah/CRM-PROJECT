# Generated by Django 4.1.7 on 2023-06-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLIENT', '0004_remove_client_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
