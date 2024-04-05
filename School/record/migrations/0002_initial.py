# Generated by Django 5.0.3 on 2024-03-27 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('record', '0001_initial'),
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sections.section', verbose_name='Секция'),
        ),
    ]
