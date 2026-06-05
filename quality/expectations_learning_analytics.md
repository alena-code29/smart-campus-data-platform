# Правила качества данных Bronze-слоя

## students

- `student_id` не должен быть пустым.
- `student_id` должен быть уникальным.
- `admission_year` должен быть в диапазоне 2020–2026.

## grades

- `student_id` не должен быть пустым.
- `grade` должен быть в диапазоне 0–100.
- `grade_date` должен быть заполнен.

## attendance

- `student_id` не должен быть пустым.
- `present` принимает только 0 или 1.
- `class_date` должен быть заполнен.

## lms_events

- `student_id` не должен быть пустым.
- `event_type` должен принимать значения `lms_login`, `material_opened`, `assignment_submitted`.
- `is_late` принимает только 0 или 1.
