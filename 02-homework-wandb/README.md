# Experiment Tracking with Weights & Biases (homework 2 wandb)
## Folders and files
- `02-wandb_instructions.md` - instructions by DTC + answered questions
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
- Go into homework 2 wandb folder (if not already)
    ```
    cd 02-homework-wandb
    ```
- Create conda environment
    ```
    conda create -n hw2b python==3.11.3
    conda activate hw2b
    pip install -r requirements.txt
    ```

## How to run the code
- Go into homework 2 wandb folder (if not already)
    ```
    cd 02-homework-wandb
    ```
- Activate conda environment (if not already)
    ```
    conda activate hw2b
    ```
- Check Weights & Biases version (Q1)
    ```
    wandb --version
    ```
- login / sign up on W&B: [wandb.ai/site](https://wandb.ai/site) & note your username

- run
    ```bash
    python preprocess_data.py \
        --wandb_project mlops-zoomcamp-wandb \
        --wandb_entity <USERNAME> \
        --raw_data_path ./data \
        --dest_path ./output
    ```
    - change `<USERNAME>` to run the command!
    - afterwards, check dv.pkl file size (Q2)
- run
    ```bash
    python train.py \
        --wandb_project mlops-zoomcamp-wandb \
        --wandb_entity <USERNAME> \
        --data_artifact "<USERNAME>/mlops-zoomcamp-wandb/NYC-Taxi:v0"
    ```
    - change `<USERNAME>` to run the command!
    - in W&B UI go to Runs -> expand -> there you will see all runs with their columns, including max_depth (Q3) & MSE

- run
    ```bash
    python sweep.py \
        --wandb_project mlops-zoomcamp-wandb \
        --wandb_entity <USERNAME> \
        --data_artifact "<USERNAME>/mlops-zoomcamp-wandb/NYC-Taxi:v0"
    ```
    - change `<USERNAME>` to run the command!
    - click on Sweeps -> on your run -> analyze hyperparameters importance (Q4)

- Create model registry and link the best model to this registry (follow the steps of Manual Linking of [this section](https://docs.wandb.ai/guides/models/walkthrough#1-create-a-new-registered-model)) (Q5)