# Generated by Django 5.0.1 on 2024-02-18 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_prod_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='prod_id',
            new_name='product',
        ),
    ]
