FROM python:3.11.3
WORKDIR /gh

COPY ["Pipfile","Pipfile.lock","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy &&\
        mkdir models
COPY ["models/sgd-classifier-dv-20240125.bin","./models/."]

COPY ["predict_model.py","./"]
EXPOSE 9696
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict_model:app" ]