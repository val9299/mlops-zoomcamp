# Deployment with FastAPI and Docker (homework 4)
By Valerie G., June 2023

## Folders and files
- `04-homework_instructions.md` - instructions by DTC + answered questions
- `Dockerfile` - to create a Docker image
- `README.md` - instructions on how to run the code
- `requirements.txt` - requirements file to create the code environment
- `app/main.py` - FastAPI code (main)
- `app/model.bin`- the model to make predictions
- `app/prediction.py` - code to make predictions (used by FastAPI code)

Note: data is directly used through an HTTP link (see main.py)
- Yellow [taxi trip duration dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) of February-April 2022 is used for homework 4

## How to run the code
- cd into homework 4 folder (if not already)
    ```
    cd 04-deployment
    ```
- Build Docker image:
  ```
  docker build -t hw4 .
  ```
    - building the Docker image will take a while when running it for the first time
    - this step only needs to be rerun when changing source code

- Run Docker image:
    ```
    docker run -p 80:80 hw4
    ```
    - this step will always be executed in order to start the Docker container to run the code

- Go to the FastAPI UI to run REST requests: http://0.0.0.0:80/docs
- To stop the Docker container from running, quit the process in the terminal (e.g., by pressing CTRL+C)

### FastAPI endpoints (with examples)
- POST /prediction_mean_std
    ```
    {
    "month": "04",
    "year": "2022"
    }
    ```
    - response:
        ```
        {
        "pred_mean": 12.865128336784926,
        "pred_std": 5.648592560412704
        }
        ```
    - this endpoints uses the Yellow Taxi Duration data of the month MM-YYYY, calculates predictions for this month, and outputs the mean and standard deviation of the predictions

### Get answers to the questions
- Q1: POST /prediction_mean_std
    ```
    {
    "month": "02",
    "year": "2022"
    }
    ```
    - answer: pred_std value

- Q5: POST /prediction_mean_std
    ```
    {
    "month": "03",
    "year": "2022"
    }
    ```
    - answer: pred_mean value

- Q6: POST /prediction_mean_std
    ```
    {
    "month": "04",
    "year": "2022"
    }
    ```
    - answer: pred_mean value
