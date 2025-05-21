FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask joblib scikit-learn numpy

EXPOSE 5002

CMD ["python", "app.py"]
