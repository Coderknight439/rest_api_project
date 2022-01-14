import os
import time
import csv
from celery import Celery
from app.database import get_session
from app.models import SchoolGradeData


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
	time.sleep(int(task_type) * 10)
	return True


@celery.task(name='populate_database')
def populate_database():
	db = get_session()
	reader = csv.DictReader(open(os.path.join("grade_data.csv")))
	data_list = []
	data = db.query(SchoolGradeData).count()
	if data <= 0:
		for raw in reader:
			data_list.append(raw)
		session = get_session()
		session.execute(SchoolGradeData.__table__.insert().values(data_list))
		session.commit()
	return True
