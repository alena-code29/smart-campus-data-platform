CREATE TABLE IF NOT EXISTS campus_events (
    event_id String,
    student_id UInt32,
    event_type String,
    event_time DateTime,
    building String,
    room String
)
ENGINE = MergeTree
ORDER BY (event_time, student_id);

CREATE VIEW IF NOT EXISTS campus_events_by_type AS
SELECT
    event_type,
    count() AS events_count
FROM campus_events
GROUP BY event_type
ORDER BY events_count DESC;
