FROM python:3.9

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip wheel 

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y gettext && \
    pip install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]