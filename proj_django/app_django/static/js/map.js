var geolocation = new ol.Geolocation({
  /*projection: view.getProjection(),*/
  tracking: true
});

setInterval(function(){
    var position= geolocation.getPosition();
    console.log(position);
    inserePonto2(position)
      /*inserePonto2(position);*/
},10000);

var map = new ol.Map({
  target:'map',
  view: new ol.View({
    center:ol.proj.fromLonLat([-49.233106,-25.450759]),
    zoom:17
  })
})

var layerOsm = new ol.layer.Tile({
  name:'osm',
  visible:'true',
  source: new ol.source.OSM()
})

map.addLayer(layerOsm);
var layerDestino = new ol.layer.Image({
  title: "Destino",
  displayInLayerSwitcher: true,
  source:new ol.source.ImageWMS({
    url:'http://localhost:8082/geoserver/banco_django/wms',
    params:{
      'LAYERS':'banco_django:destino',
    },
    ratio:1,
    serverType:'geoserver'
    })
})

var layertree = new ol.layer.Image({
  title: "Árvores",
  displayInLayerSwitcher: true,
  source:new ol.source.ImageWMS({
    url:'http://localhost:8082/geoserver/banco_django/wms',
    params:{
      'LAYERS':'banco_django:tree',
    },
    ratio:1,
    serverType:'geoserver'
    })
})
map.addLayer(layertree)



var layerBarreira = new ol.layer.Image({
  title: "Barreiras Repentinas",
  displayInLayerSwitcher: true,
  source:new ol.source.ImageWMS({
    url:'http://localhost:8082/geoserver/banco_django/wms',
    params:{
      'LAYERS':'banco_django:posicao',
    },
    ratio:1,
    serverType:'geoserver'
    })
})
map.addLayer(layerBarreira)

var layerRota = new ol.layer.Image({
  title: "Rota otimizada",
  displayInLayerSwitcher: true,
  source:new ol.source.ImageWMS({
    url:'http://localhost:8082/geoserver/banco_django/wms',
    params:{
      'LAYERS':'banco_django:rota',
    },
    ratio:1,
    serverType:'geoserver'
    })
})
map.addLayer(layerRota)


map.addLayer(layerDestino)

var layerPosUser = new ol.layer.Image({
  title: "Localização Atual",
  displayInLayerSwitcher: true,
  source:new ol.source.ImageWMS({
    url:'http://localhost:8082/geoserver/banco_django/wms',
    params:{
      'LAYERS':'banco_django:posicao_user',
    },
    ratio:1,
    serverType:'geoserver'
    })
})
map.addLayer(layerPosUser)








function inserePonto2(posicao){
  var json = {"id":id_usuario, "ponto":[posicao[0],posicao[1]]}
  $.ajax({
    url:"insereposicao2",
    type:"POST",
    headers:{
      "X-CSRFToken":token
    },
    data:json,
    dataType:'json',
    success: function(result){
      layerBarreira.getSource().updateParams({"time": Date.now()})
      layerDestino.getSource().updateParams({"time": Date.now()})
      layerPosUser.getSource().updateParams({"time": Date.now()})
      layerRota.getSource().updateParams({"time": Date.now()})
    },
    error: function(error){
      alert("Impossivel Atualizar a posição: Servidor Offline")
    }
  })
}





function inserePonto(posicao,des){
  var json = {"id":id_usuario, "ponto":[posicao[0],posicao[1]],"desc":des}
  $.ajax({
    url:"insereposicao",
    type:"POST",
    headers:{
      "X-CSRFToken":token
    },
    data:json,
    dataType:'json',
    success: function(result){
      layerBarreira.getSource().updateParams({"time": Date.now()})
    },
    error: function(error){
      alert(error)
    }
  })
}

map.on('click',function(e){
  var coordenadas =e.coordinate;
  var coordenadasSirgas = ol.proj.transform(coordenadas,'EPSG:3857','EPSG:4326')
  var des = prompt('Digite a descrição:','Ex: Obra')
  inserePonto(coordenadasSirgas,des);
})

// Add a new button to the list
var switcher = new ol.control.LayerSwitcher({
   target:$(".layerSwitcher").get(0),
   // displayInLayerSwitcher: function (l) { return false; },
   show_progress:true,
   extent: true,
   trash: true,
   oninfo: function (l) { alert(l.get("title")); }
 });

switcher.on('drawlist', function(e) {
  var layer = e.layer;
  $('<div>').text('?')// addClass('layerInfo')
    .click(function(){
      alert(layer.get('title'));
    })
    .appendTo($('> .ol-layerswitcher-buttons', e.li));
});
// Add a button to show/hide the layers
var button = $('<div class="toggleVisibility" title="show/hide">')
  .text("Show/hide all")
  .click(function() {
    var a = map.getLayers().getArray();
    var b = !a[0].getVisible();
    if (b) button.removeClass("show");
    else button.addClass("show");
    for (var i=0; i<a.length; i++) {
      a[i].setVisible(b);
    }
  });
switcher.setHeader($('<div>').append(button).get(0))

mapa.addControl(switcher);
