# Feast Feature Store

## Команды

```bash
cd feature_store/feature_repo
feast apply
feast feature-views list
```

## Feature View

`student_risk_features` регистрирует признаки из Gold-таблицы:

- `avg_grade`
- `attendance_rate`
- `lms_activity_score`
- `late_submissions`
- `campus_visits`
- `risk_score`
- `risk_level`
