# Desafio Framework usando Flask

# Como usar - Localmente:

1-Instalação do ambiente virtual

```
$ pip install virtualenv
```

2-Criar um novo ambiente virtual

```
$ virtualenv venv
```

3-Ativar o ambiente virtual

```
$ .\env\Scripts\activate
```

4-Instalar as dependências

```
$ pip install -r requirements.txt
```

5-Executar a aplicação

```
$ python app.py
```

# Docker

. Build usando Dockerfile - usando o Powershell no Windows ou bash no Linux

``` 
docker image build -t docker-desafio-framework -f ./docker/Dockerfile .
```