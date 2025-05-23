#!/bin/bash

echo "🔍 Buscando contenedores que usan puertos entre 8501 y 8509..."
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" | grep -E "850[1-9]" || echo "✅ No hay contenedores usando esos puertos."

echo ""
read -p "¿Quieres detener y eliminar todos los contenedores que usan esos puertos? (s/N): " CONFIRM

if [[ "$CONFIRM" =~ ^[sS]$ ]]; then
  IDS=$(docker ps -a --format "{{.ID}} {{.Ports}}" | grep -E "850[1-9]" | cut -d' ' -f1)
  for ID in $IDS; do
    NAME=$(docker inspect --format='{{.Name}}' $ID | sed 's,^/,,')
    echo "🧨 Eliminando contenedor: $NAME ($ID)"
    docker stop $ID >/dev/null 2>&1
    docker rm $ID >/dev/null 2>&1
  done
  echo "✅ Contenedores eliminados."
else
  echo "⏹️ Cancelado por el usuario."
fi

echo ""
echo "📡 Estado de los puertos 8501–8509 ahora:"
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" | grep -E "850[1-9]" || echo "✅ Todos los puertos están libres."
