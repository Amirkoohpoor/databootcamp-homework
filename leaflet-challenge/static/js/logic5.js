var plates;
var myMap;
var plates_url = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json";

    
    var earthquakes_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";

    

    d3.json(earthquakes_url,function(data){
    console.log(data);
   
    function Circle(feature,latlng){
        var options = {
            radius:feature.properties.mag*4,
            fillColor: chooseColor(feature.properties.mag),
            color: "black",
            weight: 1,
            opacity: 1,
        }
        return L.circleMarker( latlng, options );

    }


    var earthQuakes = L.geoJSON(data,{
        onEachFeature: function(feature,layer){
            layer.bindPopup("Place:"+feature.properties.place + "<br> Magnitude: "+feature.properties.mag+"<br> Time: "+new Date(feature.properties.time));
        },
        pointToLayer: Circle

    });

    Map(earthQuakes);

    });

  function  Map(earthQuakes) {

    var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.pirates",
      accessToken: API_KEY
    });

  
    var baseMaps = {
      "Outdoors": outdoors
    };

    var overlayMaps = {
      "Tectonic Plates": plates,
      Earthquakes: earthQuakes
    };

    var myMap = L.map("map", {
      center: [
        43,-79
      ],
      zoom: 4,
      layers: [outdoors, earthQuakes]
    });
  
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);

    var legend = L.control({
        position: "bottomright"
    });

    legend.addTo(myMap);

  }


  function chooseColor(mag){
    switch(true){

        case (mag<2):
            return "green";
        case (mag<5):
            return "yellow";
        default:
            return "red";
    };
}   