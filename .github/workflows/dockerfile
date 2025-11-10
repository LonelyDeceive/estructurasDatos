# Dockerfile (Receta completa para la imagen)
FROM python:3.11-slim

WORKDIR /app

# Optimización por cache de capas: instalamos primero dependencias.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código final.
COPY . .

# Comando de inicio del servidor Uvicorn en el puerto 80.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]