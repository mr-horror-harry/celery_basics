from celery import Celery

import os
from dotenv import load_dotenv
load_dotenv()

rabbitmq = os.environ['RABBITMQ_BROKER']
app = Celery('tasks', broker=rabbitmq)

# celery beat config
app.config_from_object('celeryconfig')

@app.task
def square(x):
    return x**2