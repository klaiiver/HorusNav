from django.contrib.gis.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Qual o seu nome?', max_length=30)
    dest = models.CharField('Qual seu destino?',max_length=100)

    class Meta:
        db_table='usuarios'
        managed=True
class Posicao(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    geom = models.PointField()
    data_criacao = models.DateField(auto_now_add=True)
    descricao = models.CharField('Descreva a barreira:', max_length=100)
    class Meta:
        db_table='posicao'
        managed=True

class Posicao_atual(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    geom = models.PointField()
    class Meta:
        db_table='posicao_atual'
        managed=True
