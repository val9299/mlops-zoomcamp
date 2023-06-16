import pickle
import pandas as pd

CATEGORICAL = ['PULocationID', 'DOLocationID']

def read_data(filepath):
    df = pd.read_parquet(filepath)
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')
    return df

def run_prediction(filepath):
    
    with open('app/model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)

    df = read_data(filepath)

    dicts = df[CATEGORICAL].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    pred_mean = float(y_pred.mean())
    pred_std = float(y_pred.std())
    
    return pred_mean, pred_std

