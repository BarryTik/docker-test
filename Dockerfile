FROM python:3.9
COPY app.py ./
CMD ["python", "./app.py"]