import json
import os
import random
import time
from datetime import datetime, timezone

from kafka import KafkaProducer

BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC = os.getenv('KAFKA_TOPIC', 'campus_student_events')
STUDENT_IDS = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
EVENT_TYPES = [
    'student_entered_campus',
    'student_left_campus',
    'lms_login',
    'material_opened',
    'assignment_submitted',
    'assignment_late',
]


def make_event():
    return {
        'event_id': f'evt-{int(time.time() * 1000)}-{random.randint(100, 999)}',
        'student_id': random.choice(STUDENT_IDS),
        'event_type': random.choice(EVENT_TYPES),
        'event_time': datetime.now(timezone.utc).isoformat(),
        'building': random.choice(['A', 'B', 'C']),
        'room': random.choice(['101', '204', '305', '410']),
    }


def main(count=50, delay=0.5):
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value, ensure_ascii=False).encode('utf-8'),
    )
    for _ in range(count):
        event = make_event()
        producer.send(TOPIC, event)
        producer.flush()
        print(f'Sent to {TOPIC}: {event}')
        time.sleep(delay)


if __name__ == '__main__':
    main()
