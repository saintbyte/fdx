# Generated by Django 2.2.4 on 2019-08-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdx_search', '0007_auto_20190824_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.CharField(default='', max_length=1024, verbose_name='Адрес'),
        ),
    ]
