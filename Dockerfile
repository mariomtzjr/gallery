FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
EXPOSE 8001:8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
