# Flask + PostgreSQL + Docker (with Adminer)

A minimal, production-like stack that runs a **Flask** app with a **PostgreSQL** database using **Docker Compose**.  
The app image is published on Docker Hub for easy pulls.

- App image: `vikrambattar/flask-app:1.0.0`  
- Or latest: `vikrambattar/flask-app:latest`

---

## 👀 What’s inside
- **Flask app** container (connects to Postgres)
- **PostgreSQL 16** with persistent volume
- **Adminer** (DB UI) at `http://localhost:8080`
- Config via `.env` (no secrets committed)

---

## 🗂 Project Structure
```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## ⚙️ Prerequisites
- Docker + Docker Compose v2 (`docker compose version`)
- macOS / Linux / Windows with Docker installed

---

## 🚀 Quick Start

1) **Create your env file**
```bash
cp .env.example .env
# edit values if needed
```

2) **Start the stack**
```bash
docker compose pull
docker compose up -d
```

3) **Verify**
- App → [http://localhost:8000](http://localhost:8000)  
- Adminer → [http://localhost:8080](http://localhost:8080)  
  - System: **PostgreSQL**  
  - Server/Host: **db**  
  - Username/Password/DB: from `.env`  
  - DB: from `.env`  

4) **Status & logs**
```bash
docker compose ps
docker logs -n 50 flask-app
docker logs -n 50 postgres-db
```

5) **Stop**
```bash
docker compose down
```

> Data persists in the `dbdata` volume. Remove with `docker volume rm <project>_dbdata` if you want a clean slate.

---

## 🧩 Configuration

**.env**
```ini
POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppass
APP_PORT=8000
```

**docker-compose.yml** (app service uses the pulled image)
```yaml
services:
  app:
    image: vikrambattar/flask-app:1.0.0
    env_file: .env
    environment:
      POSTGRES_HOST: db
    ports:
      - "${APP_PORT:-8000}:8000"
    depends_on:
      - db
```

---

## 🔒 Security Notes
- `.env` is for local development only — don’t commit real secrets for production.
- For production, use Docker/K8s secrets or a secret manager (e.g., AWS Secrets Manager, HashiCorp Vault).
- Pin image digests if you need immutable deploys.

---

## 🧪 Troubleshooting

**Port already in use**
```bash
# change APP_PORT in .env, e.g. 9000
docker compose up -d --force-recreate
```

**DB not ready / connection errors**
```bash
docker compose ps
docker exec -it postgres-db pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB"
docker logs -n 100 postgres-db
```

**App logs**
```bash
docker logs -n 100 flask-app
```

---

## 📦 Re-pulling a new version
If the Docker Hub image updates:
```bash
docker compose pull
docker compose up -d --force-recreate
```


