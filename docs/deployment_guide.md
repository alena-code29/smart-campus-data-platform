# Инструкция по развертыванию

## Требования

- Docker Desktop
- Python 3.10+
- Terraform 1.5+
- Git

## Локальный запуск

```bash
docker compose up -d
docker ps
```

## Проверка интерфейсов

- Prefect: http://localhost:4200
- MinIO: http://localhost:9001
- Grafana: http://localhost:3000
- Cube.js: http://localhost:4000

## Создание bucket в MinIO

1. Открыть http://localhost:9001.
2. Войти: `admin` / `admin12345`.
3. Создать bucket: `smart-campus-data-lake`.

## Запуск batch pipeline

```bash
pip install -r requirements.txt
python pipelines/load_raw_to_bronze.py
python quality/validate_bronze.py
python pipelines/bronze_to_silver.py
python pipelines/silver_to_gold.py
```

## Запуск Streamlit

```bash
streamlit run app/streamlit_app.py
```

## Terraform

```bash
cd infra/terraform
terraform init
terraform validate
```

## Остановка стенда

```bash
docker compose down
```
