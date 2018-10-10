FROM python:3.6-slim
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn -b 0.0.0.0:$PORT wsgi:app