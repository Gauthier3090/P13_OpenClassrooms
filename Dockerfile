FROM python:3-alpine

LABEL author='Gauthier Pladet'

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKERHUB_USER $DOCKERHUB_USER
ENV DOCKERHUB_PASSWORD $DOCKERHUB_PASSWORD
ENV PORT 8080

COPY . .

RUN python3 -m pip install -r requirements.txt --no-cache-dir
CMD python manage.py runserver 0.0.0.0:$PORT
