import pandas as pd
from pycaret.classification import predict_model, load_model

def load_data(prepped_Churn_data):
    """
    Loads diabetes data into a DataFrame from a string filepath.
    """
    df = pd.read_csv(prepped_Churn_data, index_col='customerID')
    return df


def make_predictions(df):
    """
    Uses the pycaret best model to make predictions on data in the df dataframe.
    """
    model = load_model('lr')
    predictions = predict_model(model, data=df)
    predictions.rename({'Label': 'churn_prediction'}, axis=1, inplace=True)
    predictions['churn_prediction'].replace({1: 'churn', 0: 'No churn'},
                                            inplace=True)
    return predictions['churn_prediction']


if __name__ == "__main__":
    df = load_data('new_churn_data.csv')
    predictions = make_predictions(df)
    print('predictions:')
    print(predictions)