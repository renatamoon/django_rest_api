# django_rest_api
Repository to upload course files and projects of DJANGO REST FRAMEWORK

## API REST
### O que é REST?

Representational State Transfer ou Transferencia Representacional de Estado.

- RESTFUL - padrão de criação de APIs. É a mesma coisa.

- Interface de comunicação HTTP e APIs. Uma API é uma forma de comunicação. 

### O que é HTTP?

- é onde a internet roda é por design, sem estado. Isso significa que toda requisição feita a um servidor é unica pois essas requisições não guardam dados (estados) entre requisição e outra.

- O REST não muda isso, mas coloca toda a responsabilidade de lembrar os dados da requisição no cliente.

- STATELESS - toda chamada feita a um servidor não guarda dados.

### ENDPOINTS

- Em uma API temos elementos chamados resources, ou recursos.

- Um recurso é um model na aplicação.

- Com esses recursos realizamos operaçoes de CRUD (create, retrieve, update e delete) através da API.

- Fazemos isso através de URIs, que são URLs internas.

- Um endpoint pode representar uma coleção ou registros, ou mesmo registro individual.

Exemplo: coleção: /api/v1/produtos

### VERBOS HTTP:** PUT, GET, POST, DELETE

---

- ENTENDENDO AS REQUESTS

Um dispositivo que faz uma requisição na nuvem/servidor.