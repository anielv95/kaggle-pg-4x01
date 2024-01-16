from flask import Flask
from flask import request
from flask import jsonify
import pickle

app = Flask("base-line-model")


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    # X = dv.transform([customer])
    # y_pred = model.predict_proba(X)[0, 1]
    # churn = y_pred >= 0.5
    output_file = "sgd-classifier.bin"
    with open(output_file, "rb") as f_in:
        dv, model = pickle.load(f_in)

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)

    result = {
        "id": customer["id"],
        "Status_C": y_pred[0, 0],
        "Status_CL": y_pred[0, 1],
        "Status_D": y_pred[0, 2],
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9695)
