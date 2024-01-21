FROM python:3.8.5-alpine as build
ARG ENVIRONMENT=prod
RUN pip install --upgrade pip

COPY . /app
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV API1_URL http://127.0.0.1:80/
ENV API2_URL http://api.127.0.0.1:80

CMD ["python", "main.py"]
# python -m uvicorn main:app --reload --port $PORT
