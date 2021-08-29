## Configurações iniciais


### Preparando ambiente

```
pip install sqlalchemy pre-commit flake8 pytest faker python-dotenv black
```

```
pip install -r requirements.txt
```

```
pre-commit install
```


### Rodar testes

altere o arquivo `docker-compose.yaml`, abixo de `build:` coloque `command: 'pytest -v -s'`

```
docker-compose up account_service
```

```
```

```
```
