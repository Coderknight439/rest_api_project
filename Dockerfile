FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./app /backend/app
COPY ./requirements.txt /backend
COPY ./alembic.ini /backend
COPY ./alembic /backend/alembic
COPY ./.env /backend
COPY ./grade_data.csv /backend
WORKDIR /backend/
RUN pip3 install -r requirements.txt