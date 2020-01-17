// function to populate HTML table
function modelTable(data, chosenModel) {

    // use d3.select() to find the div for model and reset html
    var tableModel = d3.select("#titleCard4");
    tableModel.html('');

    // use .append() to add a <table> tag
    var tTable = tableModel.append("table");

    // change the <table> class for bootstrap css
    tableModel.select("table").attr("class", "table table-striped")
    tableModel.select("table").style("font-size", "18px");
    tableModel.select("table").style("color", "black");
    tableModel.select("table").style("text-align", "left");
    tableModel.select("table").style("padding", "10px 10px");


    // use .append() to add a <thead> tag, do not add <tr.
    tTable.append("thead");
    
    // use .append() to add a <tbody> tag, <tr> will be added later
    tTable.append("tbody");

    // get the entries foe the object
    var keyArray = Object.keys(data);
    // console.log(keyArray);

    var lakeObject = {
        erie: "Lake Erie",
        huron: "Lake Huron",
        ontario: "Lake Ontario",
        superior: "Lake Superior",
        weighted: "Weighted Average"
    }

    arrayArrays = [
        ["F1 Scores", "Training Data", "Testing Data"],
        [lakeObject[keyArray[0]], data[keyArray[0]]["train"], data[keyArray[0]]["test"]],
        [lakeObject[keyArray[1]], data[keyArray[1]]["train"], data[keyArray[1]]["test"]],
        [lakeObject[keyArray[2]], data[keyArray[2]]["train"], data[keyArray[2]]["test"]],
        [lakeObject[keyArray[3]], data[keyArray[3]]["train"], data[keyArray[3]]["test"]],
        [lakeObject[keyArray[4]], data[keyArray[4]]["train"], data[keyArray[4]]["test"]]
    ]
    // console.log(arrayArrays);

    // use d3 to add <tr> and <td> containing the keys and values
    tableModel.select("tbody")
        .selectAll("tr")
        .data(arrayArrays)
        .enter()
        .append("tr")
        .html(function(d) {
        return `<td><b>${d[0]}</b></td><td>${d[1]}</td><td>${d[2]}</td>`;
        });
}


// function to get the API json
function getData() {

    // get the model
    var chosenModel = d3.select("#chosenModel").property("value");

    // dynamic query
    var query = `http://localhost:5000/api/f1_score?chosen_model=${chosenModel}`;

    d3.json(query).then(function(data) {

        // console.log() the data
        console.log(chosenModel);
        console.log(data);

        modelTable(data, chosenModel)
    });
}

// initialize function on page load
getData();

// when new option is selected redraw the table
d3.selectAll("#chosenModel").on("change", getData);