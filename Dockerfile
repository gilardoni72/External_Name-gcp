FROM python:3.8.5-alpine
RUN pip install Flask
RUN pip install Flask-MySQL
RUN pip install PyMySQL

COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
#RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]
