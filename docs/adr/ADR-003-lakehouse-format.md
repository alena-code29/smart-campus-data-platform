# ADR-003: Выбор формата хранения

## Статус

Принято.

## Контекст

Задание требует Lakehouse с Bronze, Silver и Gold слоями и поддержкой ACID через Delta Lake или Apache Iceberg.

## Решение

Для учебного MVP используется Parquet как базовый аналитический формат. Архитектура подготовлена к расширению до Delta Lake / Apache Iceberg через Spark.

## Последствия

Файлы Bronze, Silver и Gold сохраняются как Parquet. В production-версии можно заменить запись Parquet на Delta/Iceberg таблицы.
