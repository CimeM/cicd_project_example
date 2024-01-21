FROM python:3.8.5-alpine as build

ARG ENVIRONMENT=prod
RUN pip install --upgrade pip

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY . /app
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV ATLAS_URI mongodb://username:passhere@mongoserver
ENV DB_NAME maindbname
ENV PORT 3000

CMD ["python", "-m",  "uvicorn", "main:app", "--port","${PORT}", "--host","0.0.0.0"]
# python -m uvicorn main:app --reload --port $PORT
