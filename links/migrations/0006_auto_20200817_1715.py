# Generated by Django 3.0.8 on 2020-08-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_auto_20200817_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/', verbose_name='头像'),
        ),
    ]
