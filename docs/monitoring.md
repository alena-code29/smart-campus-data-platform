# Monitoring и Observability

## Уровни наблюдаемости

1. **Prefect UI** — статусы flow и task.
2. **Validation scripts** — контроль качества данных.
3. **MinIO Console** — проверка файлов Bronze, Silver, Gold.
4. **Kafka / Redpanda logs** — состояние потоковых событий.
5. **ClickHouse** — проверка таблиц и агрегатов.
6. **Grafana** — визуальные real-time метрики.
7. **Streamlit** — бизнес-аналитика и drill-down.
8. **Docker logs** — диагностика контейнеров.

## Возможные алерты

- Падение Prefect flow.
- Ошибка quality validation.
- Отсутствие новых событий в Kafka.
- Недоступность ClickHouse.
- Увеличение числа студентов с высоким риском.
- Ошибка загрузки данных в Data Lake.

## Пример Telegram/Slack alert

При падении задачи можно отправлять сообщение:

```text
Smart Campus pipeline failed: load_raw_to_bronze
Check Prefect logs and data quality report.
```
