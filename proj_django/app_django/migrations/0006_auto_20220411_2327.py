# Generated by Django 2.2.12 on 2022-04-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0005_posicao_atual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posicao_atual',
            name='id_po',
            field=models.AutoField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
