# saqr.com

## Project Detail

You can find all technologies we used in our project into these files:
* Version: 1.0.0
* Back-End: Django 3.2.3
* Language: Python 3.9.4
* Front-End: React
* OS: Linux (Ubuntu18.04 dist.)
* Platforms: (Web, )
* DevOps Pipline
  * Python 3.9.4
  * Django 3.2.3
  * Front: React
  * Docker + Swarm
  * Ubuntu
  * Git / Github
  * Redis
  * RabbitMQ
  * Ansible
  * Prometheus
  * Grafana
  * Postgres
  * Nginx

## Git Rules
- [Git Flow Rules](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## Django Run Server

Before creating django project you must first create virtualenv.

``` shell
$ python3.9 -m pip install virtualenv
$ python3.9 -m virtualenv venv
```

To activate virtualenvironment in ubuntu:
```shell
$ source venv\bin\activate
```

To deactive vritualenvironment use:
``` shell
$ deactivate
```

After activation must install all packages:
```shell
$ pip install -r requirements.txt
```

## Celery
Run celery worker in gps_process queue
```shell
$ celery -A kernel worker -l info -Q gps_process
```

## Docker Container

The project is dockerized for deployment.

Docker files are stored in /docs/pipe directory.
move theme to project's root directory then follow the steps below:
```shell
$ docker-compose up --build
```

## Getting Started

1. Config Django Application
2. config setting from ***settings-template.ini***

3. Database Creation Commands:

``` sql
CREATE USER semics WITH PASSWORD '1234';
CREATE DATABASE freewifi;
ALTER ROLE semics SET client_encoding TO 'utf8';
ALTER ROLE semics SET default_transaction_isolation TO 'read committed';
ALTER ROLE semics SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE freewifi TO semics;
```

4. To create all database tables:
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

5. To generate JWT private key & public key:
```shell
$ ssh-keygen -t rsa -b 4096 -m PEM -f jwt-key
$ openssl rsa -in jwt-key -pubout -outform PEM -out jwt-key.pub
```

6. Deployment Check
```shell
$ python manage.py collectstatic
$ python manage.py check
$ python manage.py test
$ python manage.py check --deploy
```

* If **psycopg2** doesn't install in ubuntu OS:
```sh
$ pip install psycopg2-binary
```