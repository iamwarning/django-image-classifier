# FROM python:3.10-alpine3.16 AS builder
FROM --platform=linux/amd64 python:3.9.14 AS builder

# Set work directory
RUN mkdir /usr/src/api
WORKDIR /usr/src/api

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=classifier.settings
ENV PATH /env/bin:$PATH

# Install psycopg2 dependencies
RUN apt-get update

# Lint
RUN pip install --upgrade pip
# RUN pip install postgresql-dev gcc python3-dev musl-dev libffi-dev
# RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.6.0-cp39-cp39-manylinux2010_x86_64.whl
RUN pip install flake8==5.0.4
COPY . .
# RUN flake8 .

# Install dependencies
COPY ./requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt
#RUN python manage.py collectstatic --no-input


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "classifier.wsgi:application"]