FROM python:3.6-alpine

# Add dependencies to install uwsgi
RUN apk add python3-dev build-base linux-headers pcre-dev gcc


WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./project ./project
ENV FLASK_APP=project/server.py
ENV FLASK_ENV=development
EXPOSE 5000

COPY ./server.ini .
CMD ["flask", "run", "--host=0.0.0.0"]
