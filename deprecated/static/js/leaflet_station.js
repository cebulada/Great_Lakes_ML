// if config.js file is missing API_KEY
if (typeof API_KEY === "undefined") {
    console.log("API_KEY NOT PRESENT", "PLEASE MAKE A config.js file in static with an API_Key");
    console.warn(`API_KEY NOT PRESENT
PLEASE MAKE A config.js file in static with an API_KEY`);
    window.alert(`API_KEY NOT PRESENT
PLEASE MAKE A config.js file in static with an API_KEY`);
} else {
    console.log("API_KEY IS PRESENT");
}

// query for the json metadata
const query = "https://great-lakes-api.herokuapp.com/api/metadata_data";

// Query the Great Lakes API
d3.json(query).then(function(data) {
    
    // console.log() the .json for more information
    console.log(data);
    /* These console.log() are how you go through the data
    console.log(data[0]);
    console.log(data[0].station);
    console.log(data[0].metadata);
    console.log(data[0].metadata.coord.latitude);
    console.log(data[0].metadata.coord.longitude);
    console.log(data[0].metadata.count);
    console.log(data[0].metadata.date.max.year);
    console.log(data[0].metadata.date.min.year);
    */

    // send the list of objects to the createFeatures function
    createFeatures(data);
});

// FUNCTION #1 //
// Function to Generate the Leaflet Plot
function createFeatures(data) {

    // ready circles array
    var markers = [];

    // for loop that iterates through and appends values to markers
    for (var i = 0; i < data.length; i++) {

        // append to markers array
        markers.push(

            // append circleMarker to circles array
            // append the latitude and longitude in [lat, long] format
            // <https://leafletjs.com/reference-1.5.0.html#circlemarker>
            L.marker([data[i].metadata.coord.latitude,
                data[i].metadata.coord.longitude])

                // Bind a popup to all the layers at once, like bindTooltip
                // bindPopup uses HTML elements which are shown below
                // <https://leafletjs.com/reference-1.5.0.html>
                .bindPopup("<h3 style='font-size:16px'>" + data[i].station +
                "</h3><hr><h4 style='font-size:12px'>Number of Measurements: " + data[i].metadata.count +
                "</h4><br><h4 style='font-size:12px'>Earliest Date(MM/DD/YYYY): " + `${data[i].metadata.date.min.month}/${data[i].metadata.date.min.day}/${data[i].metadata.date.min.year}` +
                "</h4><br><h4 style='font-size:12px'>Latest Date(MM/DD/YYYY): " + `${data[i].metadata.date.max.month}/${data[i].metadata.date.max.day}/${data[i].metadata.date.max.year}` + "</h4>")
        );
    }
    // console.log() the circles array
    console.log(markers);

    // call up createMap() function to form the map in <div id="map">
    createMap(markers);
}

// FUNCTION #3 //
// This function is responsible for taking in the array of circleMarkers
// Create a map in <div id="map">
function createMap(markers) {

    // streetmap layer
    var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.streets",
        accessToken: API_KEY
    });

    // darkmap layer
    var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.dark",
        accessToken: API_KEY
    });

    // satellite layer
    var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.satellite",
        accessToken: API_KEY
    });

    // light layer
    var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.light",
        accessToken: API_KEY
    });

    // outdoors layer
    var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.outdoors",
        accessToken: API_KEY
    });

    // Define a baseMaps object to hold our mapbox base layers
    var baseMaps = {
        "Street Map": streetmap,
        "Light / Greyscale Map": light,
        "Dark Map": darkmap,
        "Satellite Map": satellite,
        "Outdoor Map": outdoors
    };

    // make a overlayer group with the circleMarkers and call it
    // earthquake
    var stations = L.layerGroup(markers);

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
        "Water Testing Stations": stations
    };

    // Create our map, giving it the streetmap and
    // earthquakes layers to display on load
    var myMap = L.map("map", {
        // for visual purposes this is a good center point
        center: [
            46.508, -82.003
        ],
        // read the docs, apparently fractional zooms are
        // allowed now
        zoom: 5,
        layers: [satellite, stations]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    // Add a scale to the map
    L.control.scale().addTo(myMap);
}