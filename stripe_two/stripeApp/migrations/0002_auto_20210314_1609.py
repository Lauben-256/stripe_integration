# Generated by Django 3.1.7 on 2021-03-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default='https://bing.com'),
            preserve_default=False,
        ),
    ]
