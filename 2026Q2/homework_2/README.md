# Запуск

```bash
docker compose up -d
```

# Адреса сервисов

## PostgreSQL

```
UI:       http://localhost:5050
email:    admin@admin.com
password: admin

host:     postgres
port:     5432
database: analytics
username: user
password: pass
```

## MinIO

```
UI:       http://localhost:9001
username: user
password: pass
API:      http://localhost:9000
```

## Jupyter

```
URL:      http://localhost:8888
token:    analytics
```


## Superset

```
URL:      http://localhost:8088
username: admin
password: admin
```