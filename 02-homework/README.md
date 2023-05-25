# How to run the code
- Activate mlops conda environment (if not already)
    ```
    conda activate mlops
    ```
    - this is the mlops conda environment which was created before (see *Pre-requirements* in ```/mlops-zoomcamp/README.md```, i.e., the README in the repo's root folder)
- Go into 02-homework folder (if not already)
    ```
    cd 02-homework
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

