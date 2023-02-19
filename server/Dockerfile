FROM python:3.10.10-slim

RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client
WORKDIR /server

COPY ./server/pyproject.toml /server/
COPY ./server/poetry.lock /server/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

COPY ./server /server