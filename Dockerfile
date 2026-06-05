FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 10000

CMD streamlit run app/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
