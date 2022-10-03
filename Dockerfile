FROM python:3-alpine

LABEL author='Gauthier Pladet'

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKERHUB_USER $DOCKERHUB_USER
ENV DOCKERHUB_PASSWORD $DOCKERHUB_PASSWORD
ENV HEROKU_APP_NAME $HEROKU_APP_NAME
ENV PORT 8080

COPY . .

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk --purge del .build-deps

RUN python3 -m pip install -r requirements.txt
RUN python3 manage.py dumpdata -o data.json

CMD python manage.py runserver 0.0.0.0:$PORT
