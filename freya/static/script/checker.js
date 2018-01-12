function checker(){
    fetch("data").then(function(response){
        response.json().then(function(pack){
            for(i in pack.features){
                feat = pack.features[i];
                feat.geometry.coordinates = ol.proj.fromLonLat(feat.geometry.coordinates)
            }
            
            Map.getLayers().item(1).setSource(
                new ol.source.Vector({
                    features: (new ol.format.GeoJSON()).readFeatures(pack)
                })
            );
        })
    });
    setTimeout(checker, 2000);
}
