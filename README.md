# Smart Campus Learning Analytics Platform

Учебный проект по дисциплине «Распределённые информационно-аналитические системы».

Проект представляет собой прототип облачной Data Platform для цифрового кампуса. Платформа собирает данные об успеваемости студентов, посещаемости занятий, активности в LMS и событиях кампуса, затем обрабатывает их в Lakehouse-архитектуре и предоставляет аналитику через Grafana и Streamlit.

## Основные компоненты

- **Infrastructure as Code:** Terraform для описания Yandex Cloud инфраструктуры.
- **Object Storage:** S3-compatible Data Lake на базе Yandex Object Storage / MinIO.
- **Orchestration:** Prefect для batch ETL/ELT пайплайнов.
- **Lakehouse:** Bronze, Silver и Gold слои в формате Parquet с архитектурной совместимостью с Delta Lake / Apache Iceberg.
- **Data Quality:** Great Expectations style expectations + validation script.
- **Streaming:** Kafka-compatible broker Redpanda.
- **Analytical DB:** ClickHouse.
- **Dashboard:** Grafana.
- **Semantic Layer:** Cube.js.
- **Embedded Analytics:** Streamlit.
- **Feature Store:** Feast.
- **CI/CD:** GitLab CI/CD.

## Домены данных

1. `learning_analytics` — оценки, посещаемость, риск академической неуспеваемости.
2. `lms_activity` — действия студентов в LMS.
3. `campus_presence` — события входа/выхода студентов в кампусе.

## Главный Data Product

`learning_analytics.student_risk_features`

Data Product содержит признаки студентов для анализа риска академической неуспеваемости:

- средний балл;
- посещаемость;
- LMS-активность;
- количество просроченных заданий;
- посещения кампуса;
- итоговый `risk_score` и `risk_level`.

## Быстрый старт

### 1. Запуск инфраструктуры локального MVP

```bash
docker compose up -d
```

Интерфейсы:

- Prefect: http://localhost:4200
- MinIO: http://localhost:9001  
  login: `admin`, password: `admin12345`
- Grafana: http://localhost:3000  
  login: `admin`, password: `admin`
- Streamlit: http://localhost:8501
- Cube.js: http://localhost:4000

### 2. Установка Python-зависимостей локально

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Batch pipeline

```bash
python pipelines/load_raw_to_bronze.py
python quality/validate_bronze.py
python pipelines/bronze_to_silver.py
python pipelines/silver_to_gold.py
```

### 4. Streaming pipeline

```bash
python streaming/event_generator.py
python streaming/clickhouse_consumer.py
```

### 5. Embedded analytics

```bash
streamlit run app/streamlit_app.py
```

## Какие скриншоты сделать

1. Структура проекта в VS Code.
2. README.md.
3. `docs/architecture.md`.
4. `docs/data_product_student_risk.md`.
5. Terraform-файлы.
6. `terraform init`.
7. `terraform validate`.
8. `docker compose up -d` и `docker ps`.
9. Prefect UI.
10. MinIO bucket `smart-campus-data-lake`.
11. Bronze/Silver/Gold слои.
12. Запуск quality validation.
13. ClickHouse с событиями.
14. Grafana dashboard.
15. Streamlit dashboard.
16. Cube.js schema.
17. `.gitlab-ci.yml`.
18. Документация и ADR.
