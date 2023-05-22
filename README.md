# MLOPs Zoomcamp 2023
By Valerie G., 2023

## Participation in MLOps Zoomcamp 2023
- MLOps Zoomcamp is an MLOps course hosted by [DataTalks.Club](https://datatalks.club/) (DTC)
- GitHub repo of the course: https://github.com/DataTalksClub/mlops-zoomcamp/
    - 2023 specific instructions: https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/cohorts/2023

___________

## Pre-requirements to run the code!
### Create conda environment
```
conda create -n mlops python
conda activate mlops
pip install -r requirements.txt
```
___________

## Homework folders & files
### 01-homework
- ```01-homework_instructions.md``` - instructions by DTC + answered questions
- ```01-homework.ipynb``` - code verifying the answers
- ```yellow_tripdata_2022-01.parquet``` - yellow taxi trip records from January 2022 (used as the training set)
- ```yellow_tripdata_2022-02.parquet``` - yellow taxi trip records from February 2022 (used as the validation set)
    - data source: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### 02-homework
- ```02-homework_instructions.md``` - instructions by DTC + answered questions
- ```README.md``` - instructions on how to run the code
- ```*.py``` - code verifying the answers
    - these scripts originate from DTC but they were modified by me in order to complete the homework
- ```data/``` - data to run the code
    - ```green_tripdata_2022-01.parquet``` - used as the training set
    - ```green_tripdata_2022-02.parquet``` - used as the validation set
    - ```green_tripdata_2022-03.parquet``` - used as the test set
    - data source: https://www1.nyc.gov/site/tlc/about/
