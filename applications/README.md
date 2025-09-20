run python app:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
run app on docker:
    docker build -t taskmanager:latest .
    docker run -p 8000:8000 taskmanager:latest