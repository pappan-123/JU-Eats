# Generated by Django 3.2.4 on 2021-09-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
