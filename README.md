# django_rest_api
Repository to upload course files and projects of DJANGO REST FRAMEWORK

## API REST
### O que é REST?

- Representational State Transfer ou Transferencia Representacional de Estado.
- RESTFUL - padrão de criação de APIs. É a mesma coisa.
- Interface de comunicação HTTP e APIs. Uma API é uma forma de comunicação. 
---

### ENDPOINTS

- Em uma API temos elementos chamados resources, ou recursos.
- Um recurso é um model na aplicação.
- Com esses recursos realizamos operaçoes de CRUD (create, retrieve, update e delete) através da API.
- Fazemos isso através de URIs, que são URLs internas.
- Um endpoint pode representar uma coleção ou registros, ou mesmo registro individual.

Exemplo: coleção: /api/v1/produtos

---
### VERBOS HTTP

- PUT
- GET
- POST
- DELETE

---

### ENTENDENDO AS REQUESTS

- Um dispositivo que faz uma requisição na nuvem/servidor.

- <b>ACESSO DA APLICAÇÃO NA ROTA</b>: `http://127.0.0.1:8000/`
- Acesso da área administrativa do Django: `http://127.0.0.1:8000/admin`

---

### COMANDOS DJANGO:

- STARTAR UM PROJETO: `django-admin startproject school`
- STARTAR UM APP: `django-admin startapp courses`
- FAZER AS MIGRAÇÕES: `python manage.py makemigrations`
- APLICAR AS MIGRAÇÕES: `python manage.py migrate`
- CRIAR UM SUPERUSUARIO: `python manage.py createsuperuser`
- SUBIR SERVIDOR LOCAL PARA ACESSO DA ROTA: `python manage.py runserver`
