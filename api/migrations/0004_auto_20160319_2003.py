# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-19 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_artboard_owner_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingredient_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('image_url', models.CharField(max_length=1000)),
                ('posision_x', models.IntegerField(null=True)),
                ('posision_y', models.IntegerField(null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='artboard',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='artboard',
            name='size_x',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artboard',
            name='size_y',
            field=models.IntegerField(null=True),
        ),
    ]