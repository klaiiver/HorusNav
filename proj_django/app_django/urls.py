from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'index$',views.index, name ='index'),
    url(r'salvar_form$',views.salvar_form, name ='salvar_form'),
    url(r'insereposicao$',views.insereposicao, name ='insereposicao'),
    url(r'insereposicao2$',views.insereposicao2, name ='insereposicao2'),
    url(r'rota$',views.my_custom_sql, name ='rota'),
]
