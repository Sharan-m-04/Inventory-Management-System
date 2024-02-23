# Generated by Django 5.0.1 on 2024-02-23 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_product_prod_id'),
        ('transactions', '0005_alter_transaction_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
    ]