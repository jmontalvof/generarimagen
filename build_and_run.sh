#!/bin/bash
read -p "👉 Introduce el puerto en el que quieres ejecutar la app (ej. 8501 o 8502): " PORT
if [ -z "$PORT" ]; then PORT=8501; fi
echo "🛠️ Construyendo imagen Docker..."
docker build -t sd3-image-generator .
echo "🐳 Ejecutando contenedor en puerto $PORT..."
if [ -f ~/.aws/credentials ]; then
  docker run -p $PORT:8501 -v ~/.aws:/root/.aws:ro sd3-image-generator
else
  docker run -p $PORT:8501 sd3-image-generator
fi
