# Generated by Django 5.0.3 on 2024-03-24 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Секция')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Заголовок:')),
                ('content', models.TextField(verbose_name='Контент:')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото:')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания:')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования:')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.categorynews')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя:')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия:')),
                ('surname', models.CharField(max_length=200, verbose_name='Отчество')),
                ('is_this_a_child', models.BooleanField(verbose_name='Это ребенок?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('time', models.TimeField(verbose_name='Время проведения')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
