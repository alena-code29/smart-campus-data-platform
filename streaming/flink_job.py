"""
Учебный пример логики Flink SQL для скользящих окон.

В локальном MVP события можно записывать в ClickHouse через clickhouse_consumer.py,
а этот файл показывает, какую агрегацию можно выполнить во Flink.
"""

FLINK_SQL = """
CREATE TABLE campus_student_events (
  event_id STRING,
  student_id INT,
  event_type STRING,
  event_time TIMESTAMP(3),
  building STRING,
  room STRING,
  WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
) WITH (
  'connector' = 'kafka',
  'topic' = 'campus_student_events',
  'properties.bootstrap.servers' = 'localhost:9092',
  'format' = 'json',
  'scan.startup.mode' = 'earliest-offset'
);

SELECT
  building,
  HOP_START(event_time, INTERVAL '1' MINUTE, INTERVAL '5' MINUTE) AS window_start,
  HOP_END(event_time, INTERVAL '1' MINUTE, INTERVAL '5' MINUTE) AS window_end,
  COUNT(*) AS events_count,
  COUNT(DISTINCT student_id) AS active_students
FROM campus_student_events
GROUP BY
  building,
  HOP(event_time, INTERVAL '1' MINUTE, INTERVAL '5' MINUTE);
"""

if __name__ == '__main__':
    print(FLINK_SQL)
