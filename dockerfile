FROM python:3.11.8-slim-bullseye


ENV PIP_DEFAULT_TIMEOUT=100 \
    #* Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1

# RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /barda

# ADD ..
# WORKDIR /code

# RUN python manage.py collectstatic --no-input

EXPOSE 8000

# ENTRYPOINT ["python", "lief/manage.py"]
#* Start the Django server
CMD ["runserver", "0.0.0.0:8000"]
