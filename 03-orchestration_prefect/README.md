# Orchestration with Prefect (homework 3)
## Folders and files
- `03-homework_instructions.md` - instructions by DTC + answered questions
- `README.md` - instructions on how to run the code
- `requirements.txt` - requirements file to create the code environment
- `*.py` - code verifying the answers
    - these scripts originate from DTC but they were modified by me in order to complete the homework
- `data/` - data to run the code
    - `green_tripdata_2023-01.parquet` - training set for Q3
    - `green_tripdata_2023-02.parquet` 
        - validation set for Q3
        - training set for Q4
    - `green_tripdata_2023-03.parquet` - validation set for Q4
    - data source: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Pre-requirements to run the code
- Go into homework 3 folder (if not already)
    ```
    cd 03-orchestration_prefect
    ```
- Create conda environment
    ```
    conda create -n hw3 python==3.11.3
    conda activate hw3
    pip install -r requirements.txt
    ```

## How to run the code - Prefect deployment locally and with Prefect Cloud
### Pre-steps
- Go into homework 3 folder (if not already)
    ```
    cd 03-orchestration_prefect
    ```
- Activate conda environment (if not already)
    ```
    conda activate hw3
    ```
- Note: Always when you open a new terminal to run code, you need to have your hw3 conda environment activated and you need to be in the homework 3 folder!!
### Running orchestration.py with Prefect ("manually")
- You need to have done the *Pre-steps*
- Configure Prefect API URL
    ```
    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
    ```
- Start Prefect server
    ```
    prefect server start
    ```
    - open the link to the Prefect UI presented to you (http://127.0.0.1:4200)

- Open a new terminal and run the Python script (note: a correct conda environment & directory is necessary)
    ```
    python orchestrate.py
    ```
- In order to do a fresh restart for the next section, delete everything created by this section, such as
    - `mlrun`, `models`, `mlflow.db` files
    - `main-flow``` in Prefect UI


### Deploy orchestration.py with Prefect (having a more automatized process) - locally
- You need to have done the *Pre-steps*
- Create new Prefect project
    ```
    prefect project init
    ```
    - this creates one folder & some files (which can be ignored for now):
        - .prefect/
        - .prefectignore
        - deployment.yaml
        - prefect.yaml
- Configure Prefect API URL (if not already)
    ```
    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
    ```
- Start Prefect server (if not already)
    ```
    prefect server start
    ```
    - open the link to the Prefect UI presented to you (http://127.0.0.1:4200)

- Open a new terminal and start a worker (note: a correct conda environment & directory is necessary)
    ```
    prefect worker start -p hw3pool -t process
    ```

- Open a new terminal and set a deployment for your code (note: a correct conda environment & directory is necessary)
    ```
    prefect deploy $PWD/orchestrate.py:main_flow -n hw3deploy -p hw3pool
    ```

- Run the deployment
    ```
    prefect deployment run main-flow/hw3deploy
    ```
    - you can then see the process running in the Prefect UI (when navigating to main-flow)

### Deploy orchestration.py with Prefect Cloud
- You need to have done the *Pre-steps*
- Login/Register at https://app.prefect.cloud/
- Create a new workspace where everything will be stored
- In order to connect through your terminal to your Prefect Cloud profile, run:
    ```
    prefect cloud login
    ```
- Create Prefect project (if not already created!)
    ```
    prefect project init
    ```
- The following steps will be the same as for running Prefect locally

- Start a worker
    ```
    prefect worker start -p hw3pool -t process
    ```

- Open a new terminal and set a deployment for your code (note: a correct conda environment & directory is necessary)
    ```
    prefect deploy $PWD/orchestrate.py:main_flow -n hw3deploy -p hw3pool
    ```

- Run the deployment
    ```
    prefect deployment run main-flow/hw3deploy
    ```
    - you can then see the process running in the Prefect UI (when navigating to main-flow)

- Note: Through Prefect Cloud UI in tab *Automations* you can create a new Automation which can send you email notifications (in step 2 you can choose -> Action Type: send a notification; Block: email)
    - more details see [Video 3.6](https://www.youtube.com/watch?v=y89Ww85EUdo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=21) of MLOps Zoomcamp (at 14 min)

________

## How to solve the homework questions
### Q3 and Q4 - Custom Run in Prefect UI (locally)
- Do all the steps from the above section *Deploy orchestration.py with Prefect*, except the last step (i.e., *Pre-steps* and all the steps from `prefect project init` to `prefect deploy $PWD/...`)
- Do a *Custom Run* from the Prefect UI (for hw3deploy)
    - There change the input paths (i.e., Parameters) and run the code
    - For Q3 you do not have to change anything because the paths are already correct
        - train_path: <absolute_path_to_data>/green_tripdata_2023-01.parquet
        - val_path: <absolute_path_to_data>/green_tripdata_2023-02.parquet
    - For Q4 change the paths to
        - train_path: <absolute_path_to_data>/green_tripdata_2023-**02**.parquet
        - val_path: <absolute_path_to_data>/green_tripdata_2023-**03**.parquet
    - In Prefect UI *Artifacts* -> *duration_model_report* you can read the RMSE Report of the last RMSE (or you can see this value reading the last validation-rmse from the logging)
### Q6 - Prefect Cloud
- Login to your Prefect Cloud profile at https://app.prefect.cloud/
- Create a Workspace (if not already created)
- Click on your Workspace and on *Automations* tab -> create a new Automation and you will see the answer for Q6 (What is the name of the second step in the Automation creation process?)