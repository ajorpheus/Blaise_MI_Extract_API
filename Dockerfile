FROM python:3.7-slim-buster

RUN apt-get update
RUN apt-get install -y gcc g++ curl gnupg

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN apt-get install -y unixodbc-dev
RUN apt-get remove -y --purge curl
RUN apt-get remove -y --purge gnupg
RUN apt-get clean
RUN apt-get autoclean

RUN mkdir -p /deploy
WORKDIR /deploy

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pymssql
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY blaise_mi_extract_api blaise_mi_extract_api
COPY instance instance
COPY gunicorn_config.py gunicorn_config.py
COPY application.py application.py

# enter application variables here
ENV FLASK_APP blaise_mi_extract_api
ENV ENV DEV

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "application:app"]