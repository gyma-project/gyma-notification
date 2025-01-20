# Microserviço de geração de relatórios e notificações

## Como executar

1. Crie um ambiente virtual
```sh
py -m venv venv
```

2. Instale as dependências:
```sh
pip install -r requirements.txt
```

3. Baixe a imagem docker do rabbitMQ

- https://hub.docker.com/_/rabbitmq

4. Suba o container docker

```sh
docker run --hostname=my-rabbit -p 8083:15672 -p 5672:5672 -d rabbitmq:3-management
```

5. Configure o arquivo .env

Utilize o arquivo .env-exemple como base e preencha os campos:

EMAIL_USER=<Email utilizado pelo microserviço>
EMAIL_APP_KEY=<Senha de app do email>

5. Execute o arquivo mainRabbit.py
```sh
py mainRabbit.py
```

6. Teste o envio com o arquivo send.py
```sh
py mainRabbit.py
```
