# import pandas to display the database as a dataframe
import pandas as pd
import numpy as np

# import os for filenames
import os
home = os.path.abspath("")
model_files = os.path.join(home, "model_files")
json_files = os.path.join(home, "json")

# import joblib to load models, scaler and imputer
from joblib import load

# For .load_model() of .h5 files and to .predict()
from tensorflow.keras.models import load_model

# In order to calculate F1 scores
from sklearn.metrics import classification_report

# sqlalchemy dependencies in order to access FAOSTAT database
# import sqlalchemy
from sqlalchemy import create_engine

# Password and user for AWS postgreSQL
from postgres import username, password

# Helper Functions
import query_flask

######################
# FUNCTION #1 - Get means of columns
######################
def etl_mean_static():

    # database connection
    rds_connection_string = f"postgresql://{username}:{password}"+\
        "@awsgreatlakes.cdb9inonioij"+\
        ".us-east-2.rds.amazonaws.com"+\
        ":5432/awsgreatlakes"
    engine = create_engine(rds_connection_string)

    # columns of interest
    data_columns = ['lake', 'conductivity', 'hardness', 'turbidity',\
        'chlorophyll', 'ammonia', 'nitrate_ite', 'aluminum', 'barium',\
        'calcium', 'carbon', 'chloride', 'chromium', 'copper', 'magnesium',\
        'manganese', 'mercury', 'molybdenum', 'phosphorus', 'potassium',\
        'silicon', 'sodium', 'strontium', 'sulphate', 'vanadium', 'zinc']
    
    # get SQL string
    SQL_string = f"SELECT {data_columns[0]}"
    for x in data_columns[1:]:
        SQL_string += f", AVG({x}) AS {x}"
    SQL_string += f" FROM data GROUP BY {data_columns[0]}"
    print(SQL_string)

    # generate pandas dataframe then to dict from SQL string
    mean_df = pd.read_sql_query(SQL_string, con=engine)
    mean_df.set_index('lake', inplace=True)
    mean_dict = mean_df.to_dict(orient="index")

    # get second SQL string
    SQL_string = f"SELECT AVG({data_columns[1]}) AS {data_columns[1]}"
    for x in data_columns[2:]:
        SQL_string += f", AVG({x}) AS {x}"
    SQL_string += " FROM data"

    # generate pandas dataframe then to dict
    total_mean_df = pd.read_sql_query(SQL_string, con=engine)
    total_mean_df.index = ['total']
    total_mean_dict = total_mean_df.to_dict(orient="index")

    # generate combined dictionary
    mean_dict['total'] = total_mean_dict['total']

    # remove AWS connection
    del engine

    # return the dictionary which will be jsonified
    return mean_dict

######################
# FUNCTION #2 - Get metadata for stations
######################
def etl_metadata_static():

# database connection
    rds_connection_string = f"postgresql://{username}:{password}"+\
        "@awsgreatlakes.cdb9inonioij"+\
        ".us-east-2.rds.amazonaws.com"+\
        ":5432/awsgreatlakes"
    engine = create_engine(rds_connection_string)

    # get dataframe of the following columns
    data_columns = ['lake', 'date_collect', 'station_descr',\
                    'latitude', 'longitude']

    # generate SQLstring
    SQLstring = f"SELECT {data_columns[0]}"
    for x in data_columns[1:]:
        SQLstring += f", {x}"
    SQLstring += f" FROM metadata"
    print(SQLstring)
    metadata_df = pd.read_sql_query(SQLstring, con=engine)
    metadata_df = metadata_df[metadata_df["station_descr"] != "-"]
    metadata_df = metadata_df[metadata_df["latitude"] != "-"]
    metadata_df = metadata_df[metadata_df["longitude"] != "-"]
    metadata_df.dropna(inplace=True)

    # lowercase the stations and capitalize the first
    # letter of word
    redone_stations = []
    for x in metadata_df["station_descr"].unique():
        x_lower = x.lower()
        split_text = x_lower.split()
        combined_text = split_text[0].capitalize()
        for y in range(len(split_text)-1):
            combined_text += " " + split_text[y+1].capitalize()
        redone_stations.append(combined_text)

    # create dictionary
    total_count = []
    for index, x in enumerate(metadata_df["station_descr"].unique()):
        count = metadata_df.loc[metadata_df['station_descr']==x].count()
        min_date = metadata_df.loc[metadata_df['station_descr']==x,\
                                        ["date_collect"]].min()
        max_date = metadata_df.loc[metadata_df['station_descr']==x,\
                                        ["date_collect"]].max()
        latitude = metadata_df.loc[metadata_df['station_descr']==x,\
                                        ["latitude"]].head(1).values[0][0]
        longitude = metadata_df.loc[metadata_df['station_descr']==x,\
                                        ["longitude"]].head(1).values[0][0]
        lake = metadata_df.loc[metadata_df['station_descr']==x,\
                                        ["lake"]].head(1).values[0][0]
        overall_dict = {
            "station": redone_stations[index],
            "metadata": {
                "lake": str(lake),
                "count": int(count[0]),
                "date": {
                    "min": {
                        "year": int(min_date[0].year),
                        "month": int(min_date[0].month),
                        "day": int(min_date[0].day)
                    },
                    "max": {
                        "year": int(max_date[0].year),
                        "month": int(max_date[0].month),
                        "day": int(max_date[0].day)
                }},
                "coord": {
                    "latitude": float(latitude),
                    "longitude": float(longitude)
                }
            }}
        total_count.append(overall_dict)

    # remove AWS connection
    del engine

    # return the dictionary which will be jsonified
    return total_count


######################
# FUNCTION #3 - Get chosen_model for f1 scores
######################
def etl_f1_score(chosen_model):

    # For local database
    rds_connection_string = f"postgresql://{username}:{password}@awsgreatlakes.cdb9inonioij.us-east-2.rds.amazonaws.com:5432/awsgreatlakes"
    engine = create_engine(rds_connection_string)

    # get train, test and encoding label dataframes
    train_df = pd.read_sql_query('select * from train_lakes', con=engine)
    test_df = pd.read_sql_query('select * from test_lakes', con=engine)
    label_df = pd.read_sql_query('select * from encoded_lakes', con=engine)

    # Create X(data) and y(labels) for the data
    y_train = train_df["lake"]
    y_test = test_df["lake"]
    y_array_train = y_train.values.copy()
    y_array_test = y_test.values.copy()
    X_train = train_df
    X_test = test_df
    X_train.drop(["lake"], axis=1, inplace=True)
    X_test.drop(["lake"], axis=1, inplace=True)
    X_array_train = X_train.values.copy()
    X_array_test = X_test.values.copy()

    # apply minmax scaler to the train and test data
    scaler_minmax = os.path.join(model_files, 'min_max_scaler.scaler')
    scaler = load(scaler_minmax)
    X_train_scaled = scaler.transform(X_array_train)
    X_test_scaled = scaler.transform(X_array_test)

    # Giant conditional statement to determine
    # how f1 score will be determined
    if chosen_model == "Random_Forest":
        
        model_path = os.path.join(model_files, 'rf_est-100.joblib')
        model = load(model_path)
        
        report = query_flask.class_report(X_train_scaled, y_array_train, X_test_scaled,\
                            y_array_test, label_df, model)
        
        jsonify_dict = query_flask.f1_score(report)
        
    elif chosen_model == "K_Nearest_Neighbours":
        
        model_path = os.path.join(model_files, 'knn_k-9.joblib')
        model = load(model_path)
        
        report = query_flask.class_report(X_train_scaled, y_array_train, X_test_scaled,\
                            y_array_test, label_df, model)
        
        jsonify_dict = query_flask.f1_score(report)
        
    elif chosen_model == "Gradient_Boosting_Classifier":
        
        model_path = os.path.join(model_files, 'Gradient_Boosted.joblib')
        model = load(model_path)
        
        report = query_flask.class_report(X_train_scaled, y_array_train, X_test_scaled,\
                            y_array_test, label_df, model)
        
        jsonify_dict = query_flask.f1_score(report)
        
    elif chosen_model == "Deep_Neural_Net":
        
        model_path = os.path.join(model_files, 'deep_neural_7_hidden_1000_epoch.h5')
        model = load_model(model_path)
        
        report = query_flask.class_report_deep(X_train_scaled, y_array_train, X_test_scaled,\
                            y_array_test, label_df, model)
        
        jsonify_dict = query_flask.f1_score(report)
    
    # remove AWS connection
    del engine

    # return the dictionary which will be jsonified
    return jsonify_dict

######################
# FUNCTION #4 - Get data for visualization of 2 parameters
######################
def etl_param_viz(first_param, second_param):

    # For local database
    rds_connection_string = f"postgresql://{username}:{password}@awsgreatlakes.cdb9inonioij.us-east-2.rds.amazonaws.com:5432/awsgreatlakes"
    engine = create_engine(rds_connection_string)

    # list of possible columns
    data_columns = ['lake', 'water_body', 'date_collect',\
        'station_num', 'sample_num', 'station_descr', 'latitude',\
        'longitude', 'conductivity', 'hardness', 'turbidity',\
        'chlorophyll', 'ammonia', 'nitrate_ite', 'aluminum',\
       'barium', 'calcium', 'carbon', 'chloride', 'chromium',\
        'copper', 'magnesium', 'manganese', 'mercury', 'molybdenum',\
        'phosphorus', 'potassium', 'silicon', 'sodium', 'strontium',\
        'sulphate', 'vanadium', 'zinc']
    possible_columns = data_columns[8:]

    # get index value of string
    x = possible_columns.index(first_param)
    y = possible_columns.index(second_param)

    # error handling
    if x == y:
        # generate the SQLstring
        SQL_string = f"SELECT EXTRACT(YEAR FROM {data_columns[2]}) AS YYYY, lake"
        SQL_string += f", AVG({possible_columns[x]}) AS {possible_columns[x]}"
        SQL_string += " FROM master_data GROUP BY YYYY, lake"
        SQL_string += " ORDER BY lake, YYYY"

        # get all the data in a dataframe
        visualize_df = pd.read_sql_query(SQL_string, con=engine)
        visualize_df.dropna(inplace=True)

        # generate the dictionary
        master_list = {}
        for z in visualize_df["lake"].unique():
            year = visualize_df.loc[visualize_df['lake']==z, ["yyyy"]]["yyyy"].tolist()
            first_param = visualize_df.loc[visualize_df['lake']==z,\
                                        [possible_columns[x]]][possible_columns[x]].tolist()
            master_dict = {
                    "year": year,
                    possible_columns[x]: first_param
                        }
            master_list[z] = master_dict
    else:
        # generate the SQLstring
        SQL_string = f"SELECT EXTRACT(YEAR FROM {data_columns[2]}) AS YYYY, lake"
        SQL_string += f", AVG({possible_columns[x]}) AS {possible_columns[x]}"
        SQL_string += f", AVG({possible_columns[y]}) AS {possible_columns[y]}"
        SQL_string += " FROM master_data GROUP BY YYYY, lake"
        SQL_string += " ORDER BY lake, YYYY"

        # get all the data in a dataframe
        visualize_df = pd.read_sql_query(SQL_string, con=engine)
        visualize_df.dropna(inplace=True)

        # generate the dictionary
        master_list = {}
        for z in visualize_df["lake"].unique():
            year = visualize_df.loc[visualize_df['lake']==z, ["yyyy"]]["yyyy"].tolist()
            first_param = visualize_df.loc[visualize_df['lake']==z,\
                                        [possible_columns[x]]][possible_columns[x]].tolist()
            second_param = visualize_df.loc[visualize_df['lake']==z,\
                                            [possible_columns[y]]][possible_columns[y]].tolist()
            master_dict = {
                    "year": year,
                    possible_columns[x]: first_param,
                    possible_columns[y]: second_param
                        }
            master_list[z] = master_dict

    # remove AWS connection
    del engine

    # return the dictionary which will be jsonified
    return master_list

######################
# FUNCTION #5 - Predict the lake
# Lots of parameters can be looked at
######################
def etl_user_dynamic(mod0, con01, har02, tur03, chl04, amm05,\
                    nit06, alu07, bar08, cal09, car10,\
                    chl11, chr12, cop13, mag14, man15,\
                    mer16, mol17, pho18, pot19, sil20,\
                    sod21, str22, sul23, van24, zin25):

    # take all the values and put it into a list
    # go through and turn any non-numeric values into None
    param_list = [
        con01, har02, tur03, chl04, amm05,\
        nit06, alu07, bar08, cal09, car10,\
        chl11, chr12, cop13, mag14, man15,\
        mer16, mol17, pho18, pot19, sil20,\
        sod21, str22, sul23, van24, zin25
    ]
    new_param_list = []
    for x in param_list:
        try:
            float(x)
            new_param_list.append(float(x))
        except:
            new_param_list.append(None)

    # reshape the list into a numpy array in shape
    # of (1, 25)
    list_array = np.array(new_param_list)
    list_reshape = list_array.reshape((1, 25))

    # for any None values impute the previously calculated
    # mean
    imputer_simple = os.path.join(home, "model_files", 'SimpleImputer.imputer')
    imp = load(imputer_simple)
    X_finite = imp.transform(list_reshape)

    # apply the min_max scaler
    scaler_minmax = os.path.join(home, "model_files", 'min_max_scaler.scaler')
    scaler = load(scaler_minmax)
    X_scaled = scaler.transform(X_finite)

    # calculate prediction for different models
    if mod0 == "Random_Forest":
        model_path = os.path.join(model_files, 'rf_est-100.joblib')
        model = load(model_path)
        prediction = model.predict(X_scaled)
    elif mod0 == "K_Nearest_Neighbours":
        model_path = os.path.join(model_files, 'knn_k-9.joblib')
        model = load(model_path)
        prediction = model.predict(X_scaled)
    elif mod0 == "Gradient_Boosting_Classifier":
        model_path = os.path.join(model_files, 'Gradient_Boosted.joblib')
        model = load(model_path)
        prediction = model.predict(X_scaled)
    elif mod0 == "Deep_Neural_Net":
        model_path = os.path.join(model_files, 'deep_neural_7_hidden_1000_epoch.h5')
        model = load_model(model_path)
        prediction = model.predict(X_scaled)
        prediction = np.argmax(prediction, axis=-1)
    
    # translate what the encoded label means
    predict_dict = {}
    if prediction[0] == 0:
        predict_dict["prediction"] = "erie"
    elif prediction[0] == 1:
        predict_dict["prediction"] = "huron"
    elif prediction[0] == 2:
        predict_dict["prediction"] = "ontario"
    elif prediction[0] == 3:
        predict_dict["prediction"] = "superior"

    # return the dictionary which will be jsonified
    return predict_dict

