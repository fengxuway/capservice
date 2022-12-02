FROM python:3.8-buster

WORKDIR /src/

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /src/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

