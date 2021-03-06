# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('moteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Moteur')),
            ],
        ),
    ]
