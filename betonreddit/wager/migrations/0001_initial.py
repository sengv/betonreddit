# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 04:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0002_auto_20160505_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_phrase', models.TextField(default='wrong')),
                ('over_under', models.IntegerField(default=1)),
                ('over', models.IntegerField(default=0)),
                ('under', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Wager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('result', models.BooleanField(default=False)),
                ('betline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wager.Betline')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player')),
            ],
        ),
    ]
