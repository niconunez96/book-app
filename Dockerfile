FROM python:3.6-alpine

# Add dependencies to install uwsgi
RUN apk add python3-dev build-base linux-headers pcre-dev gcc


WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./project ./project
ENV ENV_CONFIG=settings.settings.DevelopmentConfig
EXPOSE 5000

COPY ./server.ini .
ENTRYPOINT [ "python" ]
CMD ["./project/server.py"]
