from celery import Celery
import time

import os
from dotenv import load_dotenv
load_dotenv()

rabbitmq = os.environ['RABBITMQ_BROKER']
app = Celery('task', broker=rabbitmq)

# celery beat config
app.config_from_object('celeryconfig')

@app.task
def square(x):
    return x**2

@app.task
def reciprocal(x):
    return x**(-1)

@app.task
def sqrt(x):
    return x**(1/2)