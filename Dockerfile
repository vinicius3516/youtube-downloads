# Usando a imagem oficial do Python com Alpine
FROM python:3.11-alpine

# Instalar dependências do sistema, incluindo FFmpeg
RUN apk update && apk add --no-cache \
    ffmpeg \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    && rm -rf /var/cache/apk/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências do projeto
COPY requirements.txt .

# Instalar as dependências (incluindo Gunicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Expor a porta do Flask
EXPOSE 5000

# Comando para rodar o servidor usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]