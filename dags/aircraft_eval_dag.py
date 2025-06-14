
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import mlflow
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def load_data():
    df = pd.read_csv('/opt/airflow/data/aircraft_landing_data.csv')
    df.to_pickle('/opt/airflow/data/preprocessed.pkl')

def train_and_log_model():
    df = pd.read_pickle('/opt/airflow/data/preprocessed.pkl')
    X = df.drop('safe_landing', axis=1)
    y = df['safe_landing']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.set_experiment("aircraft_landing_safety")
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_metric("accuracy", acc)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('mlflow_aircraft_landing_eval',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    t2 = PythonOperator(
        task_id='train_and_log_model',
        python_callable=train_and_log_model
    )

    t1 >> t2
