# FastAPI Todo & ShortURL Services

Проект состоит из двух независимых FastAPI-сервисов, запущенных в Docker.

## Сервисы
- **Todo Service** — http://localhost:8000  
  Документация: http://localhost:8000/docs
- **Short URL Service** — http://localhost:8001  
  Документация: http://localhost:8001/docs

## Требования
- Docker
- Make
- Python 3.9+ (только для тестов)

## Запуск сервисов
Из корня проекта:
```bash
make up
```

## Полная очистка (контейнеры + данные)
```bash
make down
```

## Запуск тестов
```bash
make test
```