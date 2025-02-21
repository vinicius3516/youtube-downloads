FROM alpine:3.21

# Instalar dependências do sistema
RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip py3-virtualenv

WORKDIR /app

# Criar um ambiente virtual
RUN python3 -m venv /venv

# Ativar o ambiente virtual e instalar as dependências
COPY requirements.txt .
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Definir o ambiente virtual como padrão
ENV PATH="/venv/bin:$PATH"

EXPOSE 5000

CMD ["python", "main.py"]
