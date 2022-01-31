<div align="center">
  <h1>Account Service — Microservice</h1>
  <h4>
    <strong>Status do projeto: </strong> <i>Incompleto</i> 🤓 🤓 🤓
  </h4>
  <!-- <a href="https://wakatime.com/badge/github/joaoo-vittor/account-service"><img src="https://wakatime.com/badge/github/joaoo-vittor/account-service.svg"></a> -->
</div>

----

## Objetivo do projeto

Criar um microsserviço utilizando a *Clean Architecture*, o serviço é responsavel por *registrar um usuário*, por *logar usuário*, por fazer *update de usuário*, por *ativar usuário*, por *desativar usuário* e por *buscar usuário*. Mas também, compartilhar dados com um serviço de gerenciamento de produtos feito com `Node.js`. O compartilhamento de dados é feito através do [CloudAMQP](https://www.cloudamqp.com/), o qual é um cluster RabbitMQ.

> Observação: O projeto ainda está em produção, sendo assim pode ocorrer mudanças.


## Documentação das rotas

> Documentação feita usando `swagger`: [Link Documentação](https://ecommerce-account-service-jvbs.herokuapp.com/api/v1/doc/)

----

## Diagrama de Classes

</br>

![registrar](digram/account-service.png)

</br>

----
## Configurações iniciais

### Criando um ambiente virtual

Para criar o ambiente virtual é necessário ter o `virtualenv` instalado.


```
virtualenv -p python3 venv
```

### Ativando o ambiente virtual

```
soure venv/bin/activate
```

### Instalando as dependências

```
pip install -r requirements.txt
```


### Configurar variáveis de ambiente

#### 1° Passo

> Crie um arquivo .env na raiz do projeto

```
  /src
    ...
    /queue
    /settings
      .env
    ...
  ...
```

#### 2° Passo

```
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:root@db/user
HASH=<tipo de algoritmo para gerar hash de senha>
PRIVATE_KEY=<private key to generate token>
AMQP_URL=<Sua AMQP URL>
```

> Crie um cluster RabbitMQ, na plataforma [CloudAMQP](https://www.cloudamqp.com/).

### Rodar o serviço

> Observação: É necessário ter o `docker` e o `docker-compose` instalado no seu computador.

🔗 Instalar docker-compose: [Link](https://docs.docker.com/compose/install/)

🔗 Instalar o docker: [Link](https://docs.docker.com/get-docker/)

```
docker-compose up
```
