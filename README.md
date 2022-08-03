# django_rest_api
Repository to upload course files and projects of DJANGO REST FRAMEWORK

## API REST
### O que é REST?

##### - link da documentação: https://www.django-rest-framework.org/

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

---

### CRIAÇÃO DA API REST

Com a aplicação Django já rodando, agora vamos fazer a instalação do Django Rest API:

- INSTALAÇÃO DO DJANGO REST API: `pip install djangorestframework markdown django-filter` (adicionando a documentação + filtros)

- INSTALLED APPS:

```
    'django_filters',
    'rest_framework',
    'courses',
```
---

### PERMISSIONS E AUTHENTICATIONS NO DJANGO REST

Se o usuário for authenticado, então ele pode usar todas as rotas de post, delete, get e update. Caso contrário, só tem acesso ao get.
Abaixo a configuração para authenticar o usuário.

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication'
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}
```

Depois adiciona o api-auth dentro de urls para que seja possível fazer a autenticação do usuário:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
```

- Página de login para autenticação e login do usuário: `http://127.0.0.1:8000/api-auth/login/`
- Para fazer logout: `http://127.0.0.1:8000/api-auth/logout/`

Conseguimos apenas autenticar o usuário via sessão porque colocamos `DEFAULT_AUTHENTICATION_CLASSES`


## SERIALIZERS

- Com algumas linhas podemos transformar nossos models em objetos json para lidar com as requisições das nossas apis.
- O serializers transformam objetos json e transformam em obj python, e vice versa (deserializers).
- Json: formato de dados textual que é facilmente lidos;

#### Modelo de Serializer:

```
from rest_framework import serializers


class RatingSerializer(serializers.ModelSerializer):
    # create extra class configs
    class Meta:
        extra_kwargs = {
            # this field here sets that the email won't be showed when you see the api, only when an user registrate
            'email': {
                'write_only': True
            }
        }
        
        model = Rating
        
        # fields you want to show when the user access the api - all of this are existing fields of the main model
        field = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'creation_date',
            'active'
        )
```