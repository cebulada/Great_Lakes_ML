# In order to calculate F1 scores
from sklearn.metrics import classification_report
import numpy as np
# These are helper functions
######################
# FUNCTION #1 - Get classification report
######################
def class_report(X_train, y_train, X_test, y_test, lake_labels_df, model):

    predictions_train = model.predict(X_train)
    predictions_test = model.predict(X_test)
    labels = lake_labels_df["lake"].tolist()
    report_train = classification_report(y_train, predictions_train,\
                               target_names=labels, output_dict=True)
    report_test = classification_report(y_test, predictions_test,\
                               target_names=labels, output_dict=True)
    total_dict = {
        "train": report_train,
        "test": report_test
    }
    return total_dict

######################
# FUNCTION #2 - Get classification report for
# deep neural net
######################
def class_report_deep(X_train, y_train, X_test, y_test, lake_labels_df, model):
    
    predictions_train = model.predict(X_train)
    predictions_test = model.predict(X_test)
    predictions_train_cat = np.argmax(predictions_train, axis=-1)
    predictions_test_cat = np.argmax(predictions_test, axis=-1)
    labels = lake_labels_df["lake"].tolist()
    report_train = classification_report(y_train, predictions_train_cat,\
                               target_names=labels, output_dict=True)
    report_test = classification_report(y_test, predictions_test_cat,\
                               target_names=labels, output_dict=True)
    total_dict = {
        "train": report_train,
        "test": report_test
    }
    return total_dict

######################
# FUNCTION #3 - Get F1 scores
######################
def f1_score(report):
    erie_train_f1 = round(report['train']['erie']["f1-score"],5)
    huron_train_f1 = round(report['train']['huron']["f1-score"],5)
    ontario_train_f1 = round(report['train']['ontario']["f1-score"],5)
    superior_train_f1 = round(report['train']['superior']["f1-score"],5)
    weighted_train_f1 = round(report['train']['weighted avg']["f1-score"],5)
    erie_test_f1 = round(report['test']['erie']["f1-score"],5)
    huron_test_f1 = round(report['test']['huron']["f1-score"],5)
    ontario_test_f1 = round(report['test']['ontario']["f1-score"],5)
    superior_test_f1 = round(report['test']['superior']["f1-score"],5)
    weighted_test_f1 = round(report['test']['weighted avg']["f1-score"],5)
    f1_dict = {
    "erie": {"train": erie_train_f1, "test": erie_test_f1},
    "huron": {"train": huron_train_f1, "test": huron_test_f1},
    "ontario": {"train": ontario_train_f1, "test": ontario_test_f1},
    "superior": {"train": superior_train_f1, "test": superior_test_f1},
    "weighted": {"train": weighted_train_f1, "test": weighted_test_f1}
    }
    return f1_dict

