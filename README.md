# Kaggle - Playground Series - Binary Classification with a Bank Churn Dataset

## Problem Description

This solution is for the Kaggle Playground Series Competition https://www.kaggle.com/competitions/playground-series-s4e1/overview and the purpose is to predict whether a customer continues with their account or closes it (e.g., churns)

The metric used to evaluate the performance is the area under the ROC curve between the predicted probability and the observed target, http://en.wikipedia.org/wiki/Receiver_operating_characteristic.

The output or the prediction for every id should be the probability that the client closes their account.

## Deploying model

The deployment is made with flask in a docker container with all the dependencies, to deploy de container in Linux you need:

1. Docker engine
2. Docker-compose

If you're a windows user you just need:

1. Docker Desktop

After that requirement matched you just need to execute inside the repository folder at the same path of docker-compose.yml file:

1. docker-compose up

To test the deployment you just need to go inside the repository folder and execute:

1. python ./src/predict-test.py

Additionally, there is a file to create the trained model, .src/train.py, as the trained model is in the repository it's not mandatory to execute 

1. python ./src/train.py

## Setting environment

If you want to execute the notebooks/eda.ipynb notebook you need to create a virtual environment and then install the packages, for Linux:

1. python3 -m virtualenv my_virtual_environment_name
2. source ./my_virtual_environment_name/bin/activate
3. pip install -r requirements.txt

For windows users:

1. python -m virtualenv my_virtual_environment_name
2. .\my_virtual_environment_name\Scripts\Activate
3. python -m pip install -r requirements.txt


## Executing eda.ipynb

To execute the notebook succesfully you need to change the repository folder path in the first cell in notebooks/eda.ipynb to your specific case. 
