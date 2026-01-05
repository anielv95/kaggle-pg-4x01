FROM python:3.11.3

WORKDIR /gh

COPY ["services/prep/Pipfile","services/prep/Pipfile.lock","./"]

RUN pip install pipenv &&\
        pipenv install --system --deploy 

COPY ["services/prep/predict_prep.py","./"]

EXPOSE 9695
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9695", "predict_prep:app" ]
