# Generated by Django 4.2.5 on 2023-09-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_shoppingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
