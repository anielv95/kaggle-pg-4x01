import pickle

from flask import Flask
from flask import request
from flask import jsonify

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder,StandardScaler
# import zipfile

# target = "Exited"
model_file = './models/sgd-classifier-dv-20240125.bin'

with open(model_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'churn_probability': float(y_pred),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)