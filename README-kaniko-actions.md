# Microservicio con Docker y GitHub Actions

Este proyecto contiene un microservicio básico empaquetado en un contenedor Docker y un workflow automatizado que construye y publica la imagen en Docker Hub mediante GitHub Actions.

## 📦 Estructura del Proyecto

```
.
├── app.py
├── Dockerfile
└── .github
    └── workflows
        └── build-docker.yml
```

## 🚀 Workflow: build-docker.yml

Este workflow:

- Se activa automáticamente en cada push a `main`
- Construye la imagen desde el `Dockerfile`
- Publica la imagen en Docker Hub como `jmontalvof/kaniko-test:latest`

## 🔐 Configuración requerida

### 1. Crear secretos en GitHub

Ve a tu repositorio → **Settings > Secrets and variables > Actions**  
Agrega los siguientes **Repository Secrets**:

- `DOCKER_USERNAME` → tu nombre de usuario en Docker Hub (`jmontalvof`)
- `DOCKER_PASSWORD` → tu contraseña o token de acceso de Docker Hub

### 2. Token personal para subir el workflow

Si haces push vía HTTPS con un **Personal Access Token**, este debe incluir:

- ✅ `repo`
- ✅ `workflow`

Genera el token en: [https://github.com/settings/tokens](https://github.com/settings/tokens)

Usa ese token como tu contraseña al hacer:

```bash
git push origin main
```

---

## 🛠 Cómo ejecutar

Una vez subas los cambios al repositorio:

1. GitHub Actions ejecutará automáticamente el workflow
2. Verás los logs en:  
   👉 https://github.com/jmontalvof/microservicio-ejemplo/actions
3. La imagen se publicará en:  
   👉 https://hub.docker.com/r/jmontalvof/kaniko-test

---

¡Listo! Ahora tu proyecto se despliega solo cada vez que haces push.
