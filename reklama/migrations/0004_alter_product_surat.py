# Generated by Django 5.0.6 on 2024-10-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reklama', '0003_product_surat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='surat',
            field=models.FileField(blank=True, default=None, upload_to='product_image'),
        ),
    ]
