# Generated by Django 2.1 on 2017-12-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeProductsWebsite', '0003_auto_20171205_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
