# Sealights home assignment
# Tech  Stack
* Django
- Django Rest Framework

* DB
PostgreSQL

# Running with Docker
1) Clone the repository
2) from inside the project direectory run:

docker-compose up -d --build

# API Documentation
http://localhost:8000/api-docs/

## To access the endpoints, run request from Postman or other similar app


# Running locally
1) Clone the repository
2) From the project directory run:

python3 manage.py migrate

3) Run server:

python3 manage.py runserver

# Testing only locally
Testing add and read notes, and conditions

To run:
python manage.py test

## Configuration notes
Configurations can be found in the .env file (which should not be on git for production)

- File size limit modifed to 1M for test purposes.

# Design document
![alt text](https://github.com/ashaffir/sealights/blob/main/sealights.jpg)
