import pickle
import os
from flask import Flask
from flask import request
from flask import jsonify

import requests

os.getenv("INTEGRATED_CONTAINER_HOST")
host = "localhost:9696"

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder,StandardScaler
# import zipfile

# model_file = './models/sgd-classifier-dv-20240125.bin'

# with open(model_file, 'rb') as f_in: 
#     dv, model = pickle.load(f_in)

app = Flask('churn_prep')

@app.route('/predict_prep', methods=['POST'])
def predict():
    mu = 37.1267454
    sigma = 54.24540351
    url = 'http://localhost:9695/predict'

    customer = request.get_json()

    customer["Age_scaled"] = (customer["Age_scaled"]-mu)/sigma

    #response = requests.post(url, json=customer).json()

    # X = dv.transform([customer])

    # y_pred = model.predict_proba(X)[0, 1]

    # result = {
    #     'churn_probability': float(y_pred),
    # }

    response = {"ans":"it works!"}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9695)