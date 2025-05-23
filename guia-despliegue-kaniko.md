# 🚀 Pasos para desplegar un microservicio con Docker + GitHub Actions

## 1. Crear el repositorio en GitHub

- Ve a [https://github.com/new](https://github.com/new)
- Nombra el repositorio (ej. `microservicio-ejemplo`)
- Marca como público
- Crea el repositorio

## 2. Preparar estructura del microservicio

```
microservicio-ejemplo/
├── app.py
├── Dockerfile
├── requirements.txt (opcional)
├── README.md
├── CHANGELOG.md
└── .github/
    └── workflows/
        └── build-docker.yml
```

**Ejemplo de app.py:**

```python
print("Hola desde el microservicio Kaniko!")
```

**Ejemplo de Dockerfile:**

```dockerfile
FROM python:3.10-slim
COPY app.py /app.py
CMD ["python", "/app.py"]
```

## 3. Subir el proyecto al repositorio

```bash
git init
git remote add origin https://github.com/tu_usuario/microservicio-ejemplo.git
git checkout -b main
git add .
git commit -m "Estructura inicial del microservicio"
git push -u origin main
```

## 4. Crear secretos en GitHub

Ir a: `Settings > Secrets and variables > Actions`

Crear:

- `DOCKER_USERNAME`: tu usuario Docker Hub
- `DOCKER_PASSWORD`: tu token de acceso personal

## 5. Subir el workflow de GitHub Actions

**Ejemplo de .github/workflows/build-docker.yml:**

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: tu_usuario/kaniko-test:latest
```

## 6. Verificar ejecución automática

Ver en:  
`https://github.com/tu_usuario/microservicio-ejemplo/actions`

## 7. Crear una release con tag (opcional)

```bash
git tag v1.0.0
git push origin v1.0.0
```

Esto activará el workflow para `kaniko-test:v1.0.0`.

## 8. Verificar en Docker Hub

👉 [https://hub.docker.com/repository/docker/tu_usuario/kaniko-test](https://hub.docker.com/repository/docker/tu_usuario/kaniko-test)
