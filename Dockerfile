FROM python:3.6-slim
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]