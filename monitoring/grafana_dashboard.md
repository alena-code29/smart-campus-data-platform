# Grafana Dashboard: Smart Campus Real-time Metrics

## Data Source

ClickHouse: `http://clickhouse:8123` внутри Docker или `http://localhost:8123` с хоста.

## Панели

1. Events by type
2. Active students last 5 minutes
3. Campus entries by building
4. LMS activity events
5. Late assignments

## Основной запрос

```sql
SELECT event_type, count() AS events_count
FROM campus_events
GROUP BY event_type
ORDER BY events_count DESC;
```

## Проверка данных

```sql
SELECT * FROM campus_events LIMIT 10;
```
