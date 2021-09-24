# Generated by Django 3.2.4 on 2021-09-22 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_menuitem_canteen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='canteen',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='canteen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.canteenlist'),
        ),
    ]
