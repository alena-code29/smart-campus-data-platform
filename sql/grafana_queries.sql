-- Events by type
SELECT event_type, count() AS events_count
FROM campus_events
GROUP BY event_type
ORDER BY events_count DESC;

-- Active students last 5 minutes
SELECT count(DISTINCT student_id) AS active_students
FROM campus_events
WHERE event_time >= now() - INTERVAL 5 MINUTE;

-- Campus entries by building
SELECT building, count() AS entries
FROM campus_events
WHERE event_type = 'student_entered_campus'
GROUP BY building
ORDER BY entries DESC;
