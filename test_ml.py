import pytest
import pandas as pd
import os
from ml.data import process_data
from ml.model import train_model
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

#Generate sample of data for testing
@pytest.fixture 
def data():
    #Path to cwd
    project_path = os.path.dirname(os.path.abspath(__file__))
    #Path to dataset
    data_path = os.path.join(project_path, "data", "census.csv")
    print(data_path)
    return pd.read_csv(data_path, nrows=25)

#Define necessary categorial features for testing
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
    ]

def test_data_access(data):
    """
    Ensure that data can be accessed and loaded into dataframe
    """
    assert isinstance(data, pd.DataFrame), \
        "Data not loaded into dataframe successfully."

def test_schema(data):
    """
    A test to ensure incoming dataset has the correct schema
    """
    # Check target classification column is in dataframe
    clas_col = 'salary'

    assert set(cat_features).issubset(data.columns), \
        "Dataframe needs requisite categorical features."
    assert clas_col in data.columns, \
        "Dataframe needs salary feature for classification."

def test_model_development(data):
    """
    Tests if model can be created and is of the correct type
    """
    #process_data is provided by default so it's reasonable to assume it works w/o testing
    X_train, y_train, encoder, lb = process_data(data, cat_features,label='salary',training=True)
    model = train_model(X_train, y_train)
    assert isinstance(model, GradientBoostingClassifier), \
        "Could not train GradientBoostingClassifier model successfully."


