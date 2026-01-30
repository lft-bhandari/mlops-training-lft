## Notebook 0- Start Here

In the first notebook, we basically setup the necessary packages and dependencies for successfully running the upcoming notebooks.
We also setup some important constants like region, session and dataset that will be used throughout the workshop or tutorial.

One of the main dependeny was setting up the MLFlow app server that would help in organizing the ML experiments.
It also guided us to upload the data into S3 bucket

## Notebook 1 - Idea development
This notebook was all about experimentation. Loading data, performing EDA, some feature engineering, ML hyperparameter tuning with cross validation and logging all the experimentation results, artifacts into ML flow app.

## Notebook 2 - Sagemaker Containers
This notebook was about running training jobs. Training script was created locally on the jupyter labspace and ran remotely as a Sagemaker job. It also included short intrduction on how can we run the sagemaker jobs as a docker container.

## Notebook 3 - Add an ML pipeline
This notebook was all about creating a pipeline for streamlining the fundamental workflows practiced in ML development cycle 
which included data preprocessing, data transformation, model training, experimentation and model evaluation.
AWS Pipelines was used to orchestrate the different steps.
