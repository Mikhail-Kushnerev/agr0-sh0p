# Generated by Django 2.2.16 on 2022-04-24 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_backend', '0004_auto_20220424_1054'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
