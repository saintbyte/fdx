# Generated by Django 2.2.4 on 2019-08-19 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Веб страница',
                'verbose_name_plural': 'Веб страницы',
            },
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Название персоны')),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Адрес')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image2page', to='fdx_search.Pages', verbose_name='Веб страница')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Faces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='face2image', to='fdx_search.Images', verbose_name='Картинка')),
                ('people', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='face2people', to='fdx_search.Peoples', verbose_name='Персона')),
            ],
            options={
                'verbose_name': 'Лицо',
                'verbose_name_plural': 'Лица',
            },
        ),
    ]
