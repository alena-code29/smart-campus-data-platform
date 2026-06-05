# Архитектура Smart Campus Learning Analytics Platform

Платформа построена по принципам Data Mesh, Lakehouse, Observability и Infrastructure as Code.

## Источники данных

- CSV-выгрузки из учебной системы: `students.csv`, `grades.csv`, `attendance.csv`.
- Симулированное API LMS: `lms_events.csv`.
- Потоковые события кампуса: входы, выходы, LMS-действия и отправки заданий.

## Домены данных

| Домен | Описание |
|---|---|
| `learning_analytics` | Успеваемость, посещаемость, риск академической неуспеваемости |
| `lms_activity` | Активность студентов в LMS |
| `campus_presence` | События физического присутствия в кампусе |

## Поток данных

```text
CSV / LMS API / Campus Events
        ↓
Bronze layer: сырые parquet-файлы
        ↓
Silver layer: очищенные и нормализованные данные
        ↓
Gold layer: аналитические витрины и признаки
        ↓
Feature Store / Semantic Layer / Dashboards
```

## Компоненты

- **Terraform** описывает облачную инфраструктуру: Object Storage, Kafka, VM.
- **MinIO / Object Storage** используется как S3-compatible Data Lake.
- **Prefect** выполняет batch ETL/ELT-пайплайны.
- **Validation scripts / Great Expectations style rules** проверяют качество данных.
- **Redpanda** принимает потоковые события как Kafka-compatible broker.
- **ClickHouse** хранит потоковые события и агрегаты.
- **Grafana** визуализирует real-time метрики.
- **Cube.js** отделяет бизнес-метрики от физических таблиц.
- **Streamlit** предоставляет embedded analytics интерфейс.
- **Feast** регистрирует признаки для ML.
- **GitLab CI/CD** автоматизирует проверки, сборку и деплой.

## Data Lineage

```text
students.csv + grades.csv + attendance.csv + lms_events.csv
        ↓ load_raw_to_bronze.py
bronze/learning_analytics/*.parquet
        ↓ bronze_to_silver.py
silver/learning_analytics/*_clean.parquet
        ↓ silver_to_gold.py
gold/learning_analytics/student_risk_features.parquet
        ↓
Feast Feature Store / Streamlit / Cube.js / аналитика
```
