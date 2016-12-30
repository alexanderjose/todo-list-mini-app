# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-29 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha_culminacion', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'Por iniciar'), (2, 'Iniciada'), (3, 'En progreso'), (4, 'Retrasada'), (5, 'Resuelta')], default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
