///////////////////////////////////////////////////////
// massive list of d3.select for parameters
// var chosenLake = d3.select("#chosenLake").property("value");
// var chosenModel = d3.select("#chosenModel").property("value");
// var con01 = d3.select("#con01").property("value");
// var har02 = d3.select("#har02").property("value");
// var tur03 = d3.select("#tur03").property("value");
// var chl04 = d3.select("#chl04").property("value");
// var amm05 = d3.select("#amm05").property("value");
// var nit06 = d3.select("#nit06").property("value");
// var alu07 = d3.select("#alu07").property("value");
// var bar08 = d3.select("#bar08").property("value");
// var cal09 = d3.select("#cal09").property("value");
// var car10 = d3.select("#car10").property("value");
// var chl11 = d3.select("#chl11").property("value");
// var chr12 = d3.select("#chr12").property("value");
// var cop13 = d3.select("#cop13").property("value");
// var mag14 = d3.select("#mag14").property("value");
// var man15 = d3.select("#man15").property("value");
// var mer16 = d3.select("#mer16").property("value");
// var mol17 = d3.select("#mol17").property("value");
// var pho18 = d3.select("#pho18").property("value");
// var pot19 = d3.select("#pot19").property("value");
// var sil20 = d3.select("#sil20").property("value");
// var sod21 = d3.select("#sod21").property("value");
// var str22 = d3.select("#str22").property("value");
// var sul23 = d3.select("#sul23").property("value");
// var van24 = d3.select("#van24").property("value");
// var zin25 = d3.select("#zin25").property("value");
///////////////////////////////////////////////////////
// first function 
function getAutofillMeans() {
    // static query to get mean data values
    var queryStatic = "https://great-lakes-api.herokuapp.com/api/mean_data";

    // get the relevant json from API
    d3.json(queryStatic).then(function(data) {

        // get value for Lake
        var chosenLake = d3.select("#chosenLake").property("value");

        // console.log() relevant data
        console.log(chosenLake);
        console.log(chosenModel);
        console.log(data);
        console.log(data[chosenLake]);

        // set the value property to a decimal number
        var con01 = d3.select("#con01").property("value", Math.round(data[chosenLake]["conductivity"]));
        var har02 = d3.select("#har02").property("value", Math.round(data[chosenLake]["hardness"]));
        var tur03 = d3.select("#tur03").property("value", Math.round(data[chosenLake]["turbidity"])*1000)/1000;
        var chl04 = d3.select("#chl04").property("value", Math.round(data[chosenLake]["chlorophyll"]));
        var amm05 = d3.select("#amm05").property("value", Math.round(data[chosenLake]["ammonia"]));
        var nit06 = d3.select("#nit06").property("value", Math.round(data[chosenLake]["nitrate_ite"]));
        var alu07 = d3.select("#alu07").property("value", Math.round(data[chosenLake]["aluminum"]));
        var bar08 = d3.select("#bar08").property("value", Math.round(data[chosenLake]["barium"]));
        var cal09 = d3.select("#cal09").property("value", Math.round(data[chosenLake]["calcium"]));
        var car10 = d3.select("#car10").property("value", Math.round(data[chosenLake]["carbon"]));
        var chl11 = d3.select("#chl11").property("value", Math.round(data[chosenLake]["chloride"]));
        var chr12 = d3.select("#chr12").property("value", Math.round(data[chosenLake]["chromium"]));
        var cop13 = d3.select("#cop13").property("value", Math.round(data[chosenLake]["copper"]));
        var mag14 = d3.select("#mag14").property("value", Math.round(data[chosenLake]["magnesium"]));
        var man15 = d3.select("#man15").property("value", Math.round(data[chosenLake]["manganese"]));
        var mer16 = d3.select("#mer16").property("value", Math.round(data[chosenLake]["mercury"]));
        var mol17 = d3.select("#mol17").property("value", Math.round(data[chosenLake]["molybdenum"]));
        var pho18 = d3.select("#pho18").property("value", Math.round(data[chosenLake]["phosphorus"]));
        var pot19 = d3.select("#pot19").property("value", Math.round(data[chosenLake]["potassium"]));
        var sil20 = d3.select("#sil20").property("value", Math.round(data[chosenLake]["silicon"]));
        var sod21 = d3.select("#sod21").property("value", Math.round(data[chosenLake]["sodium"]));
        var str22 = d3.select("#str22").property("value", Math.round(data[chosenLake]["strontium"]));
        var sul23 = d3.select("#sul23").property("value", Math.round(data[chosenLake]["sulphate"]));
        var van24 = d3.select("#van24").property("value", Math.round(data[chosenLake]["vanadium"]));
        var zin25 = d3.select("#zin25").property("value", Math.round(data[chosenLake]["zinc"]));
    });
}

// second function to fill with actual values
function getAutofillPaper() {

    // reference to the paper
    // Journal of Great Lakes Research 38 (2012) 550–560
    // doi:10.1016/j.jglr.2012.06.010
    // I am using the 2009 data
    var dictJournal = {
        erie: {
            calcium: 32.11*1000000,
            magnesium: 8.89*1000000,
            sodium: 8.58*1000000,
            potassium: 1.431*1000000,
            chloride: 14.58*1000000,
            sulphate: 22.81*1000000,
            conductivity: 274.06,
            hardness: 88.9*1000000
        },
        huron: {
            calcium: 26.40*1000000,
            magnesium: 7.46*1000000,
            sodium: 3.86*1000000,
            potassium: 0.939*1000000,
            chloride: 6.58*1000000,
            sulphate: 15.83*1000000,
            conductivity: 215.9,
            hardness: 78.5*1000000
        },
        ontario: {
            calcium: 33.55*1000000,
            magnesium: 8.61*1000000,
            sodium: 11.56*1000000,
            potassium: 1.501*1000000,
            chloride: 19.56*1000000,
            sulphate: 25.54*1000000,
            conductivity: 305.32,
            hardness: 90.08*1000000
        },
        superior: {
            calcium: 13.62*1000000,
            magnesium: 2.83*1000000,
            sodium: 1.44*1000000,
            potassium: 0.505*1000000,
            chloride: 1.42*1000000,
            sulphate: 3.85*1000000,
            conductivity: 102.3,
            hardness: 41.9*1000000
        },
        total: {
            calcium: 26.42*1000000,
            magnesium: 6.9475*1000000,
            sodium: 6.36*1000000,
            potassium: 1.094*1000000,
            chloride: 10.535*1000000,
            sulphate: 17.0075*1000000,
            conductivity: 224.395,
            hardness: 74.845*1000000
        }
    }

    // get value for Lake
    var chosenLake = d3.select("#chosenLake").property("value");
    console.log(dictJournal[chosenLake]);

    // set the value property to a decimal number
    var con01 = d3.select("#con01").property("value", Math.round(dictJournal[chosenLake]["conductivity"]));
    var har02 = d3.select("#har02").property("value", Math.round(dictJournal[chosenLake]["hardness"]));
    var cal09 = d3.select("#cal09").property("value", Math.round(dictJournal[chosenLake]["calcium"]));
    var chl11 = d3.select("#chl11").property("value", Math.round(dictJournal[chosenLake]["chloride"]));
    var mag14 = d3.select("#mag14").property("value", Math.round(dictJournal[chosenLake]["magnesium"]));
    var pot19 = d3.select("#pot19").property("value", Math.round(dictJournal[chosenLake]["potassium"]));
    var sod21 = d3.select("#sod21").property("value", Math.round(dictJournal[chosenLake]["sodium"]));
    var sul23 = d3.select("#sul23").property("value", Math.round(dictJournal[chosenLake]["sulphate"]));
}

// third function to submit the value properties in the input field to the API
function getPrediction() {

    // get all parameter values
    var chosenLake = d3.select("#chosenLake").property("value");
    var chosenModel = d3.select("#chosenModel").property("value");
    var con01 = d3.select("#con01").property("value");
    var har02 = d3.select("#har02").property("value");
    var tur03 = d3.select("#tur03").property("value");
    var chl04 = d3.select("#chl04").property("value");
    var amm05 = d3.select("#amm05").property("value");
    var nit06 = d3.select("#nit06").property("value");
    var alu07 = d3.select("#alu07").property("value");
    var bar08 = d3.select("#bar08").property("value");
    var cal09 = d3.select("#cal09").property("value");
    var car10 = d3.select("#car10").property("value");
    var chl11 = d3.select("#chl11").property("value");
    var chr12 = d3.select("#chr12").property("value");
    var cop13 = d3.select("#cop13").property("value");
    var mag14 = d3.select("#mag14").property("value");
    var man15 = d3.select("#man15").property("value");
    var mer16 = d3.select("#mer16").property("value");
    var mol17 = d3.select("#mol17").property("value");
    var pho18 = d3.select("#pho18").property("value");
    var pot19 = d3.select("#pot19").property("value");
    var sil20 = d3.select("#sil20").property("value");
    var sod21 = d3.select("#sod21").property("value");
    var str22 = d3.select("#str22").property("value");
    var sul23 = d3.select("#sul23").property("value");
    var van24 = d3.select("#van24").property("value");
    var zin25 = d3.select("#zin25").property("value");

    // make this massive query
    var baseQuery = "https://great-lakes-api.herokuapp.com/api/guess?";
    var queryDynamic1 = baseQuery + `mod0=${chosenModel}&lake=${chosenLake}&con01=${con01}`;
    var queryDynamic2 = queryDynamic1 + `&har02=${har02}&tur03=${tur03}&chl04=${chl04}&amm05=${amm05}`;
    var queryDynamic3 = queryDynamic2 + `&nit06=${nit06}&alu07=${alu07}&bar08=${bar08}&cal09=${cal09}`;
    var queryDynamic4 = queryDynamic3 + `&car10=${car10}&chl11=${chl11}&chr12=${chr12}&cop13=${cop13}`;
    var queryDynamic5 = queryDynamic4 + `&mag14=${mag14}&man15=${man15}&mer16=${mer16}&mol17=${mol17}`;
    var queryDynamic6 = queryDynamic5 + `&pho18=${pho18}&pot19=${pot19}&sil20=${sil20}&sod21=${sod21}`;
    var queryDynamic7 = queryDynamic6 + `&str22=${str22}&sul23=${sul23}&van24=${van24}&zin25=${zin25}`;

    // console.log() the query
    console.log(queryDynamic7);

    // get the relevant json from API
    d3.json(queryDynamic7).then(function(data) {

        // console.log() the data
        console.log(data);

        // get the values from the json
        var lakeChosen = data["chosen_lake"];
        var modelChosen = data["chosen_model"];
        var predictionGuess = data["prediction"];

        predictionDict = {
            erie: "Lake Erie",
            huron: "Lake Huron",
            ontario: "Lake Ontario",
            superior: "Lake Superior",
            total: "All 4 Great Lakes"
        };

        // set the value property for these text boxes
        var lakeGuess = d3.select("#selectLake").property("value", predictionDict[lakeChosen]);
        var lakePrediction = d3.select("#guessLake").property("value", predictionDict[predictionGuess]);
    });
}

// clear function
function getClear() {

    // clear all values
    var lakeGuess = d3.select("#selectLake").property("value", "");
    var lakePrediction = d3.select("#guessLake").property("value", "");
    var con01 = d3.select("#con01").property("value", "");
    var har02 = d3.select("#har02").property("value", "");
    var tur03 = d3.select("#tur03").property("value", "");
    var chl04 = d3.select("#chl04").property("value", "");
    var amm05 = d3.select("#amm05").property("value", "");
    var nit06 = d3.select("#nit06").property("value", "");
    var alu07 = d3.select("#alu07").property("value", "");
    var bar08 = d3.select("#bar08").property("value", "");
    var cal09 = d3.select("#cal09").property("value", "");
    var car10 = d3.select("#car10").property("value", "");
    var chl11 = d3.select("#chl11").property("value", "");
    var chr12 = d3.select("#chr12").property("value", "");
    var cop13 = d3.select("#cop13").property("value", "");
    var mag14 = d3.select("#mag14").property("value", "");
    var man15 = d3.select("#man15").property("value", "");
    var mer16 = d3.select("#mer16").property("value", "");
    var mol17 = d3.select("#mol17").property("value", "");
    var pho18 = d3.select("#pho18").property("value", "");
    var pot19 = d3.select("#pot19").property("value", "");
    var sil20 = d3.select("#sil20").property("value", "");
    var sod21 = d3.select("#sod21").property("value", "");
    var str22 = d3.select("#str22").property("value", "");
    var sul23 = d3.select("#sul23").property("value", "");
    var van24 = d3.select("#van24").property("value", "");
    var zin25 = d3.select("#zin25").property("value", "");
}




