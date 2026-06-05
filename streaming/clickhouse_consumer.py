import json
import os
from kafka import KafkaConsumer
import clickhouse_connect

BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC = os.getenv('KAFKA_TOPIC', 'campus_student_events')
CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST', 'localhost')
CLICKHOUSE_PORT = int(os.getenv('CLICKHOUSE_PORT', '8123'))

client = clickhouse_connect.get_client(host=CLICKHOUSE_HOST, port=CLICKHOUSE_PORT)

client.command('''
CREATE TABLE IF NOT EXISTS campus_events (
    event_id String,
    student_id UInt32,
    event_type String,
    event_time DateTime,
    building String,
    room String
)
ENGINE = MergeTree
ORDER BY (event_time, student_id)
''')

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda value: json.loads(value.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='smart-campus-clickhouse-consumer',
)

print(f'Listening topic: {TOPIC}')
for message in consumer:
    event = message.value
    client.insert(
        'campus_events',
        [[
            event['event_id'],
            int(event['student_id']),
            event['event_type'],
            event['event_time'][:19].replace('T', ' '),
            event.get('building', ''),
            event.get('room', ''),
        ]],
        column_names=['event_id', 'student_id', 'event_type', 'event_time', 'building', 'room'],
    )
    print(f'Inserted into ClickHouse: {event}')
