FROM python:3.12-slim

WORKDIR /app

COPY "eleida2.py" .

CMD ["python", "eleida2.py"]