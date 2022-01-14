from app.tasks import populate_database


def run_celery_start_task():
	populate_database.delay()
	return True


if __name__ == '__main__':
	run_celery_start_task()
