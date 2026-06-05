from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_source_files_exist():
    for name in ['students.csv', 'grades.csv', 'attendance.csv', 'lms_events.csv']:
        assert (ROOT / 'data' / 'raw' / name).exists()
