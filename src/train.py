import sys
sys.path.insert(1, '/gh/kaggle-pg-4x01')
import zipfile
import pandas as pd

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
#from sklearn.metrics import log_loss
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import pickle
import src.functions as func
import requests
import seaborn as sn
from sklearn.linear_model import SGDClassifier


target = "Exited"


with zipfile.ZipFile("./data/playground-series-s4e1.zip") as z:
    with z.open("train.csv") as f:
        train = pd.read_csv(f)


strat_train_set, strat_test_set = train_test_split(
    train, test_size=0.2, stratify=train[[target,"IsActiveMember"]], random_state=42)


min_outlier = 17.0
max_outlier = 57.0

strat_train_set = strat_train_set[strat_train_set["Age"]<=max_outlier].copy()

std_scaler = StandardScaler()
strat_train_set["Age_scaled"] = std_scaler.fit_transform(strat_train_set[["Age"]])

selected_features = ["IsActiveMember","Age_scaled"]
#training function

def train(df_train, y_train):
    dicts = df_train[selected_features].to_dict(orient="records")
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    model = SGDClassifier(loss="log_loss", max_iter=5,random_state=42)
    model.fit(X_train,y_train)
    return dv, model

# X = strat_train_set[selected_features].values
# y = strat_train_set[target].values

# clf = SGDClassifier(loss="log_loss", max_iter=5,random_state=42)
# clf.fit(X, y)

# error = roc_auc_score(strat_train_set[target],y_hat[:,1])
# print(error)

def predict(df,dv,model):
    dicts = df[selected_features].to_dict(orient='records')
    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred

# Validation

clf2 = SGDClassifier(loss="log_loss", max_iter=5,random_state=42)

scores = cross_val_score(clf2, strat_train_set[selected_features], strat_train_set[target],
                              scoring="roc_auc", cv=10)

print('validation results:')
print(' %.3f +- %.3f' % (scores.mean(), scores.std()))

#training the final model

strat_test_set["Age_scaled"] = std_scaler.transform(strat_test_set[["Age"]])

dv,model = train(strat_train_set,strat_train_set[target])

# X_test = strat_test_set[selected_features].values

y_hat_test = predict(strat_test_set,dv,model)

y_test = strat_test_set[target].values

error = roc_auc_score(y_test,y_hat_test)
error

print(f'auc={error}')

output_file = './models/sgd-classifier-dv-20240125.bin'
with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')