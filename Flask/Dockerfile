FROM python:3.9.6-alpine3.14

RUN apk add --update && apk add ca-certificates

COPY ./requirements.txt /
COPY ./flask/ /flask

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/flask/flaskhello.py"]
