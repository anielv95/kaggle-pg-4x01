FROM python:3.11.3
WORKDIR /gh

COPY ["Pipfile","Pipfile.lock","src/predict.py","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy &&\
        mkdir models
COPY ["models/sgd-classifier-dv-20240125.bin","./models/."]
EXPOSE 9695
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9695", "predict:app" ]