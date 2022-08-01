# Generated by Django 4.0.6 on 2022-07-31 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_shop', '0013_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_In_Wrork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_info', models.CharField(max_length=2000000, verbose_name='Дані про замовлення')),
                ('adress', models.CharField(max_length=2000, verbose_name='Адреса користувача')),
                ('additional_info', models.CharField(max_length=2000, verbose_name='Додаткова інформація')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]