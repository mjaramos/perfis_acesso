# Imagem oficial do Python
FROM python:3.11-slim

# Diretório da aplicação
WORKDIR /app

# Copiar tudo para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Fly.io usa a porta 8080
ENV PORT=8080
EXPOSE 8080

# Iniciar o servidor Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]