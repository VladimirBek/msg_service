FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
COPY . /app

ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
