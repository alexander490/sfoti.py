import time
from celery import task

@task
def demorada():
	time.sleep(5)
	print('Acebe !')