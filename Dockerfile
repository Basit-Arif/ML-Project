FROM python:3.11

WORKDIR /app
COPY . /app


RUN apt update -y

RUN pip install -r requirements.txt
EXPOSE 5005
CMD ["python","app.py"]

