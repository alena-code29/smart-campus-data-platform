from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64, String

student = Entity(
    name='student',
    join_keys=['student_id'],
    description='Student entity for Smart Campus Learning Analytics',
)

student_risk_source = FileSource(
    path='../../data/lake/gold/learning_analytics/student_risk_features.parquet',
    timestamp_field=None,
)

student_risk_features = FeatureView(
    name='student_risk_features',
    entities=[student],
    ttl=timedelta(days=1),
    schema=[
        Field(name='avg_grade', dtype=Float32),
        Field(name='attendance_rate', dtype=Float32),
        Field(name='lms_activity_score', dtype=Int64),
        Field(name='late_submissions', dtype=Int64),
        Field(name='campus_visits', dtype=Int64),
        Field(name='risk_score', dtype=Float32),
        Field(name='risk_level', dtype=String),
    ],
    online=True,
    source=student_risk_source,
)
