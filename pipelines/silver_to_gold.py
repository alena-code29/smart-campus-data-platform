from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SILVER_DIR = PROJECT_ROOT / 'data' / 'lake' / 'silver' / 'learning_analytics'
GOLD_DIR = PROJECT_ROOT / 'data' / 'lake' / 'gold' / 'learning_analytics'
GOLD_DIR.mkdir(parents=True, exist_ok=True)


def calculate_risk(row):
    grade_risk = max(0, (75 - row['avg_grade']) / 75)
    attendance_risk = max(0, 1 - row['attendance_rate'])
    lms_risk = max(0, 1 - min(row['lms_activity_score'] / 5, 1))
    late_risk = min(row['late_submissions'] / 3, 1)
    return round(0.4 * grade_risk + 0.3 * attendance_risk + 0.2 * lms_risk + 0.1 * late_risk, 3)


def risk_level(score):
    if score >= 0.6:
        return 'high'
    if score >= 0.3:
        return 'medium'
    return 'low'


def build_student_risk_features():
    students = pd.read_parquet(SILVER_DIR / 'students_clean.parquet')
    grades = pd.read_parquet(SILVER_DIR / 'grades_clean.parquet')
    attendance = pd.read_parquet(SILVER_DIR / 'attendance_clean.parquet')
    lms = pd.read_parquet(SILVER_DIR / 'lms_events_clean.parquet')

    grade_features = grades.groupby('student_id').agg(avg_grade=('grade', 'mean')).reset_index()
    attendance_features = attendance.groupby('student_id').agg(attendance_rate=('present', 'mean')).reset_index()
    lms_features = lms.groupby('student_id').agg(
        lms_activity_score=('event_type', 'count'),
        late_submissions=('is_late', 'sum')
    ).reset_index()

    campus_visits = lms.groupby('student_id').size().reset_index(name='campus_visits')
    result = students.merge(grade_features, on='student_id', how='left')
    result = result.merge(attendance_features, on='student_id', how='left')
    result = result.merge(lms_features, on='student_id', how='left')
    result = result.merge(campus_visits, on='student_id', how='left')

    for column in ['avg_grade', 'attendance_rate', 'lms_activity_score', 'late_submissions', 'campus_visits']:
        result[column] = result[column].fillna(0)

    result['avg_grade'] = result['avg_grade'].round(2)
    result['attendance_rate'] = result['attendance_rate'].round(2)
    result['risk_score'] = result.apply(calculate_risk, axis=1)
    result['risk_level'] = result['risk_score'].apply(risk_level)

    output = GOLD_DIR / 'student_risk_features.parquet'
    result.to_parquet(output, index=False)
    result.to_csv(GOLD_DIR / 'student_risk_features.csv', index=False)
    return output, result


if __name__ == '__main__':
    output, df = build_student_risk_features()
    print(f'Gold table created: {output}')
    print(df[['student_id', 'full_name', 'avg_grade', 'attendance_rate', 'risk_score', 'risk_level']])
