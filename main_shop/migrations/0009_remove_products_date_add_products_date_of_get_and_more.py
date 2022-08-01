# Generated by Django 4.0.3 on 2022-07-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0008_products_date_add_alter_products_product_png'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='date_add',
        ),
        migrations.AddField(
            model_name='products',
            name='Date_of_get',
            field=models.DateField(auto_now=True, verbose_name='Дата отримання'),
        ),
        migrations.AddField(
            model_name='products',
            name='number_of_prouct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='кількість товару'),
        ),
        migrations.AddField(
            model_name='products',
            name='unit_of_measure',
            field=models.CharField(default=0, max_length=150, verbose_name='Одиниці вимірювання'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_png',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='main_shop\\static\\main_shop\\img\\%Y\\%m\\%d'),
        ),
    ]