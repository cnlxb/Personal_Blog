# Generated by Django 3.0.8 on 2020-08-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20200817_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media/avatar', verbose_name='头像'),
        ),
    ]
