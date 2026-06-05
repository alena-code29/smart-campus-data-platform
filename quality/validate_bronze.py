from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BRONZE_DIR = PROJECT_ROOT / 'data' / 'lake' / 'bronze' / 'learning_analytics'


def assert_no_nulls(df: pd.DataFrame, column: str, dataset: str):
    if df[column].isna().any():
        raise AssertionError(f'{dataset}: column {column} contains null values')


def assert_between(df: pd.DataFrame, column: str, low: float, high: float, dataset: str):
    if not df[column].between(low, high).all():
        raise AssertionError(f'{dataset}: column {column} must be between {low} and {high}')


def validate_students():
    df = pd.read_parquet(BRONZE_DIR / 'students.parquet')
    assert_no_nulls(df, 'student_id', 'students')
    if df['student_id'].duplicated().any():
        raise AssertionError('students: student_id must be unique')
    assert_between(df, 'admission_year', 2020, 2026, 'students')
    return len(df)


def validate_grades():
    df = pd.read_parquet(BRONZE_DIR / 'grades.parquet')
    assert_no_nulls(df, 'student_id', 'grades')
    assert_between(df, 'grade', 0, 100, 'grades')
    return len(df)


def validate_attendance():
    df = pd.read_parquet(BRONZE_DIR / 'attendance.parquet')
    assert_no_nulls(df, 'student_id', 'attendance')
    assert_between(df, 'present', 0, 1, 'attendance')
    return len(df)


def validate_lms_events():
    df = pd.read_parquet(BRONZE_DIR / 'lms_events.parquet')
    assert_no_nulls(df, 'student_id', 'lms_events')
    allowed = {'lms_login', 'material_opened', 'assignment_submitted'}
    unknown = set(df['event_type']) - allowed
    if unknown:
        raise AssertionError(f'lms_events: unknown event types: {unknown}')
    assert_between(df, 'is_late', 0, 1, 'lms_events')
    return len(df)


if __name__ == '__main__':
    results = {
        'students': validate_students(),
        'grades': validate_grades(),
        'attendance': validate_attendance(),
        'lms_events': validate_lms_events(),
    }
    print('Data quality validation completed successfully')
    for dataset, rows in results.items():
        print(f'- {dataset}: {rows} rows validated')
