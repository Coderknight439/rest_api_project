import os
import time

from celery import Celery
import psycopg2
from app.config import settings

connection = psycopg2.connect(
		f"host='{settings.POSTGRES_SERVER}'"
		f"dbname='{settings.POSTGRES_DB}'"
		f"user='{settings.POSTGRES_USER}'"
		f"password='{settings.POSTGRES_PASSWORD}'"
)
cursor = connection.cursor()

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
	time.sleep(int(task_type) * 10)
	return True


@celery.task(name='populate_database')
def populate_database():
	with open('../grade_data.csv', 'r') as f:
		next(f)  # Skip the header row.
		cursor.copy_from(f, 'school_grade_data', sep=',')
	
	connection.commit()
	return True
