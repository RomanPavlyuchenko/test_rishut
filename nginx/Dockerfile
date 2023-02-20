FROM python:3.10.10-slim AS server

RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client netcat
WORKDIR /server

COPY ./server/pyproject.toml /server/
COPY ./server/poetry.lock /server/
COPY ./server/entrypoint.sh /server/
RUN chmod +x /server/entrypoint.sh

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./server /server

ENTRYPOINT ["/server/entrypoint.sh"]

#########################################

FROM nginx:1.19.2

RUN rm -v /etc/nginx/nginx.conf
ADD ./nginx/nginx.conf /etc/nginx/

RUN mkdir /nginx
COPY --from=server /server/static /nginx/static