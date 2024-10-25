FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR  /app
COPY service_hw5.py predict.py
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696","predict:app" ]