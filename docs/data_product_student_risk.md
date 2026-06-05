# Data Product: learning_analytics.student_risk_features

## Назначение

Data Product предназначен для анализа риска академической неуспеваемости студентов и подготовки признаков для ML-модели.

## Домен

`learning_analytics`

## Владельцы

Команда цифровой аналитики университета.

## Источники

- `students.csv`
- `grades.csv`
- `attendance.csv`
- `lms_events.csv`
- `campus_student_events` Kafka topic

## Выходная таблица

`student_risk_features`

## Основные поля

| Поле | Описание |
|---|---|
| `student_id` | Уникальный идентификатор студента |
| `full_name` | ФИО студента |
| `faculty` | Факультет |
| `group_id` | Учебная группа |
| `avg_grade` | Средний балл |
| `attendance_rate` | Доля посещённых занятий |
| `lms_activity_score` | Индекс активности в LMS |
| `late_submissions` | Количество просроченных заданий |
| `campus_visits` | Количество посещений кампуса |
| `risk_score` | Итоговый риск от 0 до 1 |
| `risk_level` | Категория риска: low, medium, high |

## SLA

- Batch-обновление: 1 раз в день.
- Real-time метрики: каждые 1–5 минут.
- Целевая доступность аналитического слоя: 99%.

## Метрики качества

- `student_id` не должен быть пустым.
- `student_id` должен быть уникальным в таблице студентов.
- `avg_grade` должен находиться в диапазоне от 0 до 100.
- `attendance_rate` должен находиться в диапазоне от 0 до 1.
- `risk_score` должен находиться в диапазоне от 0 до 1.
- `risk_level` должен принимать значения `low`, `medium`, `high`.

## Потребители

- Учебный отдел.
- Руководители образовательных программ.
- ML-модели прогноза риска.
- Streamlit dashboard.
- Grafana dashboard.
