# Generated by Django 4.0.3 on 2022-07-31 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0018_alter_orders_user_id_alter_preorder_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product_id',
            field=models.CharField(default=0, max_length=200, verbose_name='Username'),
        ),
    ]