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
    """List all available api routes."""
    return (
        f"Available Routes: <br/>"

        f"<a href='/api/mean_data'>/api/mean_data</a><br/>"

        f"<a href='/api/metadata_data'>/api/metadata_data</a><br/>"

        f"<a href='/api/f1_score?chosen_model=Deep_Neural_Net'>/api/f1_score?chosen_model=Deep_Neural_Net</a><br/>"

        f"<a href='/api/viz_years?first_param=conductivity&second_param=chlorophyll'>/api/viz_years?first_param=conductivity&second_param=chlorophyll</a><br/>"

        f"<a href='/api/guess?mod0=Random_Forest&lake=erie&con01=270&tur03=2.7'>/api/guess?mod0=Random_Forest&lake=erie&con01=270&tur03=2.7</a><br/>"
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