# Generated by Django 2.2.12 on 2022-02-17 00:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, verbose_name='Qualo seu nome?')),
                ('idade', models.IntegerField(verbose_name='Qual sua idade?')),
            ],
            options={
                'db_table': 'usuarios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Posicao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('id_usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_django.Usuarios')),
            ],
            options={
                'db_table': 'posicao',
                'managed': True,
            },
        ),
    ]