# Generated by Django 3.2.4 on 2021-09-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_auto_20210923_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
