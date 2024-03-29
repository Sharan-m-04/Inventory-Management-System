# Generated by Django 5.0.1 on 2024-02-18 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0006_alter_product_prod_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_quantity', models.IntegerField()),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
