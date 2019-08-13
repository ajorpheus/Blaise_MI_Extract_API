FROM python:3.6-alpine

RUN mkdir -p /deploy
WORKDIR /deploy

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY api_template api_template
COPY instance instance
COPY gunicorn_config.py gunicorn_config.py
COPY application.py application.py

# enter application variables here
ENV FLASK_APP api_template
ENV ENV DEV

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "application:app"]