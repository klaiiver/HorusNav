# Generated by Django 2.2.12 on 2022-04-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0008_auto_20220411_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posicao_atual',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Qual o seu nome?'),
        ),
        migrations.AlterModelTable(
            name='posicao_atual',
            table='posicao_atual',
        ),
    ]
