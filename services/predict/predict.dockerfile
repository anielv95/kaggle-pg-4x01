FROM python:3.11.3
WORKDIR /gh

COPY ["services/predict/Pipfile","services/predict/Pipfile.lock","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy &&\
        mkdir models
COPY ["models/sgd-classifier-dv-20240125.bin","./models/."]

COPY ["services/predict/predict_model.py","./"]
EXPOSE 9696
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict_model:app" ]
