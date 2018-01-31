# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171028_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date', models.DateField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to='core.Child')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'Weight',
                'ordering': ['-date'],
            },
        ),
    ]
