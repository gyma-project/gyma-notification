# Use uma imagem base do Python
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 5672

RUN apt-get update && apt-get install -y dnsutils && rm -rf /var/lib/apt/lists/*

# Comando para rodar a aplicação
CMD ["python", "mainRabbit.py"]
