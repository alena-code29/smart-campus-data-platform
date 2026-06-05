python scripts/create_minio_bucket.py
python pipelines/load_raw_to_bronze.py
python quality/validate_bronze.py
python pipelines/bronze_to_silver.py
python pipelines/silver_to_gold.py
