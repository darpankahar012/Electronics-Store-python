# Generated by Django 2.2.14 on 2020-07-15 13:02

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_order_billing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
