FROM python:latest
WORKDIR /app
COPY . /app

RUN pip install flask mysql-connector-python
CMD ["python", "webserver.py"]