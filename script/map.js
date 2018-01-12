var OSMlayer = new ol.layer.Tile({
    source: new ol.source.OSM()
});

var CanLayer = new ol.layer.Vector({
    style: CanStyle
});

var View = new ol.View({
    center: ol.proj.transform([0, 0], 'EPSG:4326', 'EPSG:3857'),
    zoom: 5
});

var Map = new ol.Map({
    target: "map",
    layers: [OSMlayer, CanLayer],
    view: View
});

checker();
