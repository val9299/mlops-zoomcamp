# Experiment Tracking & Model Registry with MLflow (homework 2)
## Folders and files
- `02-homework_instructions.md` - instructions by DTC + answered questions
- `README.md` - instructions on how to run the code
- `requirements.txt` - requirements file to create the code environment
- `*.py` - code verifying the answers
    - these scripts originate from DTC but they were modified by me in order to complete the homework
- `data/` - data to run the code
    - `green_tripdata_2022-01.parquet` - used as the training set
    - `green_tripdata_2022-02.parquet` - used as the validation set
    - `green_tripdata_2022-03.parquet` - used as the test set
    - data source: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Pre-requirements to run the code
- Go into homework 2 folder (if not already)
    ```
    cd 02-experiment-tracking_mlflow
    ```
- Create conda environment
    ```
    conda create -n hw2 python==3.11.3
    conda activate hw2
    pip install -r requirements.txt
    ```

## How to run the code
- Go into homework 2 folder (if not already)
    ```
    cd 02-experiment-tracking_mlflow
    ```
- Activate conda environment (if not already)
    ```
    conda activate hw2
    ```
- Check MLFlow version (Q1)
    ```
    mlflow --version
    ```
- pre-process data
    ```
    python ./preprocess_data.py --raw_data_path ./data --dest_path ./output
    ```
    - afterwards, check dv.pkl file size (Q2)
- run
    ```
    python ./train.py
    ```
    - run
        ```
        mlflow ui --backend-store-uri sqlite:///mlflow.db
        ```
    - Experiment "02-homework-Q3" -> click on the one run -> Parameters -> max_depth (Q3)

- run
    ```
    python ./hpo.py
    ```
    - run (if not still running)
        ```
        mlflow ui --backend-store-uri sqlite:///mlflow.db
        ```
    - Experiment "random-forest-hyperopt" -> read best RMSE (on validation set) (Q4)

- run
    ```
    python ./register_model.py
    ```
    - Q5 answer will be printed to system output
    - run (if not still running)
        ```
        mlflow ui --backend-store-uri sqlite:///mlflow.db
        ```
    - investigate "Models" tab (Q6)
