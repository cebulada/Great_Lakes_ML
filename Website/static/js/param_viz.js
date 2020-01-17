// choose which titles to display
function getTitles(analyte, chosenLake, mapTitles) {
    var index = mapTitles.analytes.indexOf(analyte);
    var dict = {
        lake: mapTitles.lakes[chosenLake],
        values: mapTitles.analytes[index],
        x_Title: mapTitles.x_Title,
        axis_Title: mapTitles.axis_Title[index],
        comparison_scatter: mapTitles.comparison_scatter
    };
    return dict;
}

// Function to draw the graphs
function drawGraphs(yearArray, firstArray, secondArray,
    firstTitle, secondTitle) {

    var trace1 = {
        x: yearArray,
        y: firstArray,
        type:"'lines+markers'"
    };
    var trace2 = {
        x: yearArray,
        y: secondArray,
        type:"'lines+markers'"
    };
    var trace4 = {
    x: yearArray, 
    y: firstArray, 
    z: secondArray,
    mode: 'markers',
    marker: {
        size: 12,
        line: {
        color: 'rgba(217, 217, 217, 0.14)',
        width: 0.5},
        opacity: 0.8},
    type: 'scatter3d'
    };
    var data1 = [trace1];
    var data2 = [trace2];
    var layout1 = {
        title: firstTitle.lake + " " + firstTitle.axis_Title,
        yaxis: {title: firstTitle.axis_Title},
        xaxis: {title: firstTitle.x_Title}
    };
    var layout2 = {
        title: secondTitle.lake + " " + secondTitle.axis_Title,
        yaxis: {title: secondTitle.axis_Title},
        xaxis: {title: secondTitle.x_Title}
    };

    Plotly.newPlot("bar1", data1, layout1);
    Plotly.newPlot("bar2", data2, layout2);
    //Plotly.newPlot("bar3", data3, layout3);
    var data4 = [trace4];
    var layout4 = {margin: {
        l: 0,
        r: 0,
        b: 0,
        t: 0
        },
        scene: {
            xaxis:{title: secondTitle.x_Title},
            yaxis:{title: firstTitle.lake + " " + firstTitle.axis_Title},
            zaxis:{title: secondTitle.lake + " " + secondTitle.axis_Title},
            camera:{eye:{x: 2.9228775723752123,
                        y: 1.095198434702106,
                        z: 1.2171607482105795}}
            }};
    Plotly.newPlot('bar3', data4, layout4);
    // get eye coordinates
    // var myPlot = document.getElementById('bar3');
    // myPlot.on('plotly_relayout', function(data){console.log(data)});
}

// First Function is to recieve data from API
function getData() {

    // get the parameters
    var chosenLake = d3.select("#chosenLake").property("value");
    var firstParam = d3.select("#chosenParam1").property("value");
    var secondParam = d3.select("#chosenParam2").property("value");

    // dynamic query
    var query = `http://localhost:5000/api/viz_years?first_param=${firstParam}&second_param=${secondParam}`;

    // get the relevant json from API
    d3.json(query).then(function(data) {

        // console.log() the data and chosen lake
        console.log(chosenLake);
        console.log(data);

        // assemble arrays for graphs
        var yearArray = data[chosenLake]["year"];
        var firstArray = data[chosenLake][firstParam];
        var secondArray = data[chosenLake][secondParam];

        // get map titles
        var mapFirstTitles = getTitles(firstParam, chosenLake, mapTitles);
        var mapSecondTitles = getTitles(secondParam, chosenLake, mapTitles);

        // feed the data into the drawGraphs() function
        drawGraphs(yearArray, firstArray, secondArray,
            mapFirstTitles, mapSecondTitles);
    });
}

// initialize the charts upon webpage loading
getData();

// when new option is selected redraw the charts
d3.selectAll("#chosenLake").on("change", getData);
d3.selectAll("#chosenParam1").on("change", getData);
d3.selectAll("#chosenParam2").on("change", getData);