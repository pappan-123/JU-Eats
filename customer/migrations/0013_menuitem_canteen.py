# Generated by Django 3.2.4 on 2021-09-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20210921_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='canteen',
            field=models.ManyToManyField(blank=True, null=True, to='customer.CanteenList'),
        ),
    ]
