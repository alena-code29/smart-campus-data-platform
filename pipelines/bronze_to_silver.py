from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BRONZE_DIR = PROJECT_ROOT / 'data' / 'lake' / 'bronze' / 'learning_analytics'
SILVER_DIR = PROJECT_ROOT / 'data' / 'lake' / 'silver' / 'learning_analytics'
SILVER_DIR.mkdir(parents=True, exist_ok=True)


def clean_students():
    df = pd.read_parquet(BRONZE_DIR / 'students.parquet')
    df = df.drop_duplicates(subset=['student_id'])
    df['student_id'] = df['student_id'].astype(int)
    df['faculty'] = df['faculty'].str.strip()
    df['group_id'] = df['group_id'].str.strip()
    df.to_parquet(SILVER_DIR / 'students_clean.parquet', index=False)
    return df


def clean_grades():
    df = pd.read_parquet(BRONZE_DIR / 'grades.parquet')
    df['student_id'] = df['student_id'].astype(int)
    df['grade'] = df['grade'].clip(0, 100)
    df['grade_date'] = pd.to_datetime(df['grade_date'])
    df.to_parquet(SILVER_DIR / 'grades_clean.parquet', index=False)
    return df


def clean_attendance():
    df = pd.read_parquet(BRONZE_DIR / 'attendance.parquet')
    df['student_id'] = df['student_id'].astype(int)
    df['class_date'] = pd.to_datetime(df['class_date'])
    df['present'] = df['present'].astype(int)
    df.to_parquet(SILVER_DIR / 'attendance_clean.parquet', index=False)
    return df


def clean_lms_events():
    df = pd.read_parquet(BRONZE_DIR / 'lms_events.parquet')
    df['student_id'] = df['student_id'].astype(int)
    df['event_time'] = pd.to_datetime(df['event_time'])
    df['is_late'] = df['is_late'].astype(int)
    df.to_parquet(SILVER_DIR / 'lms_events_clean.parquet', index=False)
    return df


if __name__ == '__main__':
    outputs = {
        'students_clean': len(clean_students()),
        'grades_clean': len(clean_grades()),
        'attendance_clean': len(clean_attendance()),
        'lms_events_clean': len(clean_lms_events()),
    }
    print('Bronze to Silver transformation completed')
    for name, rows in outputs.items():
        print(f'- {name}: {rows} rows')
