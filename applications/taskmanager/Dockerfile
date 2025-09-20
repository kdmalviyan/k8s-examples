FROM python:3.11-slim

WORKDIR /app
EXPOSE 8000

COPY ./applications/taskmanager/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./applications/taskmanager/app ./app

# Use uvicorn with --workers for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

