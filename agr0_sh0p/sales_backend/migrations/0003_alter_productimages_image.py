# Generated by Django 3.2.12 on 2022-02-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_backend', '0002_alter_productimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/product_group/product/'),
        ),
    ]
