# Generated by Django 5.0.6 on 2024-10-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reklama', '0002_alter_category_options_alter_category_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='surat',
            field=models.FileField(default=1, upload_to='product_image'),
            preserve_default=False,
        ),
    ]
