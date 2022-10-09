FROM python:3-alpine

LABEL author='Gauthier Pladet'

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN
ENV DOCKERHUB_USER $DOCKERHUB_USER
ENV DOCKERHUB_PASSWORD $DOCKERHUB_PASSWORD
ENV HEROKU_APP_NAME $HEROKU_APP_NAME
ENV PORT 8080

COPY . .

RUN apt-get update && apt-get -y upgrade
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk --purge del .build-deps

CMD python3 -m pip install -r requirements.txt
CMD python manage.py collectstatic --no-input
CMD python3 manage.py dumpdata -o data.json
CMD python manage.py runserver 0.0.0.0:$PORT
