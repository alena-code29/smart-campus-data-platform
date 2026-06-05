# Semantic Layer и Embedded Analytics

## Semantic Layer

В проекте используется Cube.js. Он отделяет физические таблицы ClickHouse от бизнес-пользователей.

## Схемы

- `Students.js` — студенты, факультеты, группы.
- `StudentRisk.js` — метрики риска и успеваемости.
- `CampusEvents.js` — события кампуса и real-time метрики.

## Бизнес-метрики

- `StudentCount`
- `AvgGrade`
- `AvgAttendanceRate`
- `HighRiskStudents`
- `AvgLmsActivity`
- `EventsCount`
- `ActiveStudents`
- `RoomEntries`
- `RoomExits`

## Embedded Analytics

Веб-интерфейс реализован на Streamlit. Он показывает:

- количество студентов;
- средний балл;
- среднюю посещаемость;
- число студентов с высоким риском;
- графики по факультетам и группам;
- таблицу Gold-слоя.

## Drill-down

Пользователь может выбрать факультет и группу в sidebar. После выбора пересчитываются метрики, графики и таблица.
