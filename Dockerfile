FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 10000

CMD sh -c "python pipelines/load_raw_to_bronze.py && python pipelines/bronze_to_silver.py && python pipelines/silver_to_gold.py && streamlit run app/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0"
