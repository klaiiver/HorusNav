from django.shortcuts import render
from . forms import Form_usuarios, Form_desc
from django.http import JsonResponse
import json
from . models import Posicao, Usuarios, Posicao_atual
from django.contrib.gis.geos import Point
from django.db import connection
import googlemaps

gmaps = googlemaps.Client(key='######')
def SelecionaInicio():
    with connection.cursor() as cursor:
        cursor.execute("SELECT osm_id FROM ways_vertices_pgr, posicao_user ORDER BY ST_Distance(ways_vertices_pgr.the_geom, posicao_user.geom ) limit 1")
        row = cursor.fetchall()
        pontoI = row[0]
        return pontoI

def SelecionaFim():
    with connection.cursor() as cursor:
        cursor.execute("SELECT dest from usuarios")
        row = cursor.fetchall()
    #user_dest = Usuarios.objects.get(dest=dest)
    user_dest = row[-1]
    result = gmaps.geocode(user_dest)
    pontoFim = str(result[0]['geometry']['location']['lng']) + ',' + str(result[0]['geometry']['location']['lat'])
    with connection.cursor() as cursor:
        cursor.execute("create or replace view destino as SELECT * FROM ways_vertices_pgr ORDER BY ST_Distance(ways_vertices_pgr.the_geom, ST_SetSRID(ST_Point(%s), 4326)) limit 1"%pontoFim)
        cursor.execute("SELECT osm_id FROM ways_vertices_pgr ORDER BY ST_Distance(ways_vertices_pgr.the_geom, ST_SetSRID(ST_Point(%s), 4326)) limit 1"%pontoFim)
        row = cursor.fetchall()
        pontoF = row[0]
        return pontoF




def my_custom_sql():
    #ponto1 = SelecionaInicio()
    ponto1 = [9597873291]
    ponto2 = SelecionaFim()
    with connection.cursor() as cursor:
        #cursor.execute("CREATE OR REPLACE VIEW rota as SELECT the_geom, dataid, waysfinal.source_osm, target_osm, waysfinal.custo FROM waysfinal JOIN(SELECT * FROM pgr_dijkstra('SELECT dataid as id, source_osm AS source, target_osm AS target, custo AS cost FROM waysfinal',%s, %s , directed => false)) AS route ON waysfinal.gid = route.edge"%(ponto1[0],ponto2[0]))
        cursor.execute("CREATE OR REPLACE VIEW rota AS SELECT the_geom, gid, waysfinal.source_osm, target_osm FROM waysfinal JOIN (SELECT * FROM pgr_dijkstra('SELECT gid as id, source_osm AS source, target_osm AS target, custo AS cost FROM waysfinal',%s, %s,directed => false)) AS route ON waysfinal.gid = route.edge"%(ponto1[0],ponto2[0]))

def index(request):
    form = Form_usuarios()
    return render(request,'index.html',{'form':form})

def salvar_form(request):
    if request.method=='POST':
        form = Form_usuarios(request.POST)
        if form.is_valid():
            result = form.save()
            id = result.id
            b=my_custom_sql()
            return render(request,'mapa.html',{'id':id})

def insereposicao(request):
    if request.is_ajax():
        if request.method =='POST':
            dicionario = dict(request.POST)
            id_usuario = dicionario['id'][0]
            descri = dicionario['desc'][0]


            ponto = Point(float(dicionario['ponto[]'][0]),float(dicionario['ponto[]'][1]))
            obj_usuario = Usuarios.objects.get(id=id_usuario)
            #descri =Form_desc(request.POST)
            obj = Posicao(id_usuarios=obj_usuario, geom=ponto,descricao=descri)
            obj.save()


            resposta = '{result:ok}'
            return JsonResponse(json.dumps(resposta),safe=False)


def insereposicao2(request):
    if request.is_ajax():
        if request.method =='POST':
            dicionario = dict(request.POST)
            id_usuario = dicionario['id'][0]

            ponto = Point(float(dicionario['ponto[]'][0]),float(dicionario['ponto[]'][1]))
            obj_usuario = Usuarios.objects.get(id=id_usuario)
            obj = Posicao_atual(id_usuarios=obj_usuario, geom=ponto)
            obj.save()


            resposta = '{result:ok}'
            #b=my_custom_sql()
            return JsonResponse(json.dumps(resposta),safe=False)
