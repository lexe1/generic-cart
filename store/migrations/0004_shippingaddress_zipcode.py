# Generated by Django 4.1.4 on 2022-12-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_products_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
