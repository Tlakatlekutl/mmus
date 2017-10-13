# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markup.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=markup.models.user_directory_path)),
                ('ready', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markup.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.PositiveSmallIntegerField()),
                ('y1', models.PositiveSmallIntegerField()),
                ('x2', models.PositiveSmallIntegerField()),
                ('y2', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markup.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markup.Tag'),
        ),
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(to='markup.Tag'),
        ),
    ]
