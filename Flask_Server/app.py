# import Flask libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
import etl_flask

# Create an instance of Flask
app = Flask(__name__)

# ensure that flask server enables CORS
CORS(app)

# default app route, list them all
@app.route("/")
def home():
    """List all available api routes and landing page."""
    return (
        f"<h1>Great Lakes Water Testing API</h1>"
        f"<h2><a href='http://localhost:8000/' target='_blank'>Link</a> to Web Visualizations hosted on Github Pages</h2>"
        f"<h2>Created by <a href='https://www.linkedin.com/in/daniel-cebula-b098b3a3/' target='_blank'>Daniel Adam Cebula</a> and <a href='https://www.linkedin.com/in/rohanchaudhari/' target='_blank'>Rohan Chaudhari</a></h1>"
        f"<hr size='10' color='black'>"

        f"<h3>Static #1:  Mean Values of Parameters for Lakes and Total</h3>"
        f"<a href='/api/mean_data' target='_blank'>/api/mean_data</a>"
        f"<p>Returns JSON of postgreSQL queried mean data</p>"
        f"<hr size='10' color='black'>"

        f"<h3>Static #2:  Metadata for Water Intake Stations and Associated Water Testing Sites</h3>"
        f"<a href='/api/metadata_data' target='_blank'>/api/metadata_data</a>"
        f"<p>Returns JSON of postgreSQL queried Station Names, Geographic Coordinates (Latitude and Longitude), Count of Samples and Date Range</p>"
        f"<hr size='10' color='black'>"

        f"<h3>Dynamic #1:  Dynamically determined F1 scores for 4 models</h3>"
        f"<a href='/api/f1_score?chosen_model=Deep_Neural_Net' target='_blank'>/api/f1_score?chosen_model=Deep_Neural_Net</a>"
        f"<p>Determine the F1 scores of training and test data for 4 models.  Can accept 1 parameter:  chosen_model=</p>"
        f"""<ul>
        <li>Random_Forest</li>
        <li>K_Nearest_Neighbours</li>
        <li>Gradient_Boosting_Classifier</li>
        <li>Deep_Neural_Net</li>
        </ul>"""
        f"<hr size='10' color='black'>"

        f"<h3>Dynamic #2:  Mean value of parameters over the years</h3>"
        f"<a href='/api/viz_years?first_param=conductivity&second_param=chlorophyll' target='_blank'>/api/viz_years?first_param=conductivity&second_param=chlorophyll</a><br/>"
        f"<p>Determine the mean value for parameters over the years in which data is available.  Can accept 2 parameters: first_param= and second_param= from this list of 25</p>"
        f"""<ol>
        <li>conductivity</li>
        <li>hardness</li>
        <li>turbidity</li>
        <li>chlorophyll</li>
        <li>ammonia</li>
        <li>nitrate_ite</li>
        <li>aluminum</li>
        <li>barium</li>
        <li>calcium</li>
        <li>carbon</li>
        <li>chloride</li>
        <li>chromium</li>
        <li>copper</li>
        <li>magnesium</li>
        <li>manganese</li>
        <li>mercury</li>
        <li>molybdenum</li>
        <li>phosphorus</li>
        <li>potassium</li>
        <li>silicon</li>
        <li>sodium</li>
        <li>strontium</li>
        <li>sulphate</li>
        <li>vanadium</li>
        <li>zinc</li>
        </ol>"""
        f"<hr size='10' color='black'>"

        f"<h3>Dynamic #3:  Given any number of parameters for a chosen model receive a prediction of which great lake the water sample was sourced from</h3>"
        f"<a href='/api/guess?mod0=Random_Forest&lake=erie&con01=270&tur03=2.7' target='_blank'>/api/guess?mod0=Random_Forest&lake=erie&con01=270&tur03=2.7</a><br/>"
        f"<p>Determine the mean value for parameters over the years in which data is available.  Need at minimum mod0 to receive a prediction.  The following list are all the parameters and what they correspond to.  All numeric values are float64(accepts decimal values):</p>"
        f"""<ol>
        <li>mod0= - Chosen Model from list in Dynamic #1</li>
        <li>lake= - User's guess to Great Lake (erie, huron, ontario, superior)</li>
        <li>con01= - Water Conductivity (Unit: &#181;S/m)</li>
        <li>har02= - Water Hardness (Unit: ng/L or ppb)</li>
        <li>tur03= - Water Turbidity (Unit: FTU)</li>
        <li>chl04= - Chlorophyll A + B (Unit: ng/L or ppb)</li>
        <li>amm05= - Ammonia (Unit: ng/L or ppb)</li>
        <li>nit06= - Nitrate and/or Nitrate (Unit: ng/L or ppb)</li>
        <li>alu07= - Aluminum (Unit: ng/L or ppb)</li>
        <li>bar08= - Barium (Unit: ng/L or ppb)</li>
        <li>cal09= - Calcium (Unit: ng/L or ppb)</li>
        <li>car10= - Carbon (Unit: ng/L or ppb)</li>
        <li>chl11= - Chloride (Unit: ng/L or ppb)</li>
        <li>chr12= - Chromium (Unit: ng/L or ppb)</li>
        <li>cop13= - Copper (Unit: ng/L or ppb)</li>
        <li>mag14= - Magnesium (Unit: ng/L or ppb)</li>
        <li>man15= - Manganese (Unit: ng/L or ppb)</li>
        <li>mer16= - Mercury (Unit: ng/L or ppb)</li>
        <li>mol17= - Molybdenum (Unit: ng/L or ppb)</li>
        <li>pho18= - Phosphorus (Unit: ng/L or ppb)</li>
        <li>pot19= - Potassium (Unit: ng/L or ppb)</li>
        <li>sil20= - Silicon (Unit: ng/L or ppb)</li>
        <li>sod21= - Sodium (Unit: ng/L or ppb)</li>
        <li>str22= - Strontium (Unit: ng/L or ppb)</li>
        <li>sul23= - Sulphate (Unit: ng/L or ppb)</li>
        <li>van24= - Vanadium (Unit: ng/L or ppb)</li>
        <li>zin25= - Zinc (Unit: ng/L or ppb)</li>
        </ol>"""

        f"<p>This is an <a href='/api/guess?mod0=Random_Forest&lake=erie&con01=280&har02=120000000&tur03=5.6&chl04=3000&amm05=27000&nit06=501753&alu07=45307&bar08=19481&cal09=33465889&car10=23876561&chl11=16011789&chr12=508&cop13=1685&mag14=9049618&man15=5966&mer16=21&mol17=1029&pho18=38295&pot19=1461226&sil20=432641&sod21=9936207&str22=155875&sul23=23183262&van24=404&zin25=1701' target='_blank'>example</a> query that results in a prediction of Erie</p>"
    )


# first API
# just the means
@app.route("/api/mean_data")
def mean_data():

    # call a function which will get
    # means in a dictionary format
    data = etl_flask.etl_mean_static()

    # return dictionary as a json
    return jsonify(data)


# second API
# just the metadata
@app.route("/api/metadata_data")
def metadata_data():

    # call a function which will get
    # means in a dictionary format
    data = etl_flask.etl_metadata_static()

    # return dictionary as a json
    return jsonify(data)

# third API
# this API takes in 1 parameter, model
@app.route("/api/f1_score")
def model_f1_score():

    # recieve a query
    chosen_model = request.args.get('chosen_model')

    # call a function which will get
    # means in a dictionary format
    data = etl_flask.etl_f1_score(chosen_model)

    # return dictionary as a json
    return jsonify(data)

# fourth API
# this API takes in 2 parameter, out of 25 params
# choose 2
@app.route("/api/viz_years")
def viz_years():

    # recieve a query for 2 parameters
    first_param = request.args.get('first_param')
    second_param = request.args.get('second_param')

    # call a function which will get
    # means in a dictionary format
    data = etl_flask.etl_param_viz(first_param, second_param)

    # return dictionary as a json
    return jsonify(data)

# fifth API
# this API takes in up to 25 parameters, out of 25 params
# choose as many as you want
# the rest become None and will be imputed
@app.route("/api/guess")
def guess():

    # massive list of potential variables
    mod0 = request.args.get('mod0')
    lake = request.args.get('lake')
    con01 = request.args.get('con01')
    har02 = request.args.get('har02')
    tur03 = request.args.get('tur03')
    chl04 = request.args.get('chl04')
    amm05 = request.args.get('amm05')
    nit06 = request.args.get('nit06')
    alu07 = request.args.get('alu07')
    bar08 = request.args.get('bar08')
    cal09 = request.args.get('cal09')
    car10 = request.args.get('car10')
    chl11 = request.args.get('chl11')
    chr12 = request.args.get('chr12')
    cop13 = request.args.get('cop13')
    mag14 = request.args.get('mag14')
    man15 = request.args.get('man15')
    mer16 = request.args.get('mer16')
    mol17 = request.args.get('mol17')
    pho18 = request.args.get('pho18')
    pot19 = request.args.get('pot19')
    sil20 = request.args.get('sil20')
    sod21 = request.args.get('sod21')
    str22 = request.args.get('str22')
    sul23 = request.args.get('sul23')
    van24 = request.args.get('van24')
    zin25 = request.args.get('zin25')

    # feed it into this function
    data = etl_flask.etl_user_dynamic(mod0, con01, har02, tur03, chl04, amm05,\
                                     nit06, alu07, bar08, cal09, car10,\
                                     chl11, chr12, cop13, mag14, man15,\
                                     mer16, mol17, pho18, pot19, sil20,\
                                     sod21, str22, sul23, van24, zin25)

    # feed back the chosen_model and chosen_lake to dictionary
    data["chosen_model"] = mod0
    data["chosen_lake"] = lake

    # return dictionary as a json
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)