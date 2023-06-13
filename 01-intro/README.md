# Intro to ML task (01-homework)
## Folders and files
- ```01-homework_instructions.md``` - instructions by DTC + answered questions
- ```01-homework.ipynb``` - code verifying the answers
- ```README.md``` - instructions on how to run the code
- ```requirements.txt``` - requirements file to create the code environment
- ```yellow_tripdata_2022-01.parquet``` - yellow taxi trip records from January 2022 (used as the training set)
- ```yellow_tripdata_2022-02.parquet``` - yellow taxi trip records from February 2022 (used as the validation set)
    - data source: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Pre-requirements to run the code
- Go into 01-homework folder (if not already)
    ```
    cd 01-homework
    ```
- Create conda environment
    ```
    conda create -n hw1 python==3.11.3
    conda activate hw1
    pip install -r requirements.txt
    ```

## How to run the code
- Go into 01-homework folder (if not already)
    ```
    cd 01-homework
    ```
- Activate conda environment (if not already)
    ```
    conda activate hw1
    ```
- Run
    ```
    jupyter notebook
    ```
