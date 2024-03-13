from celery import Celery

import os
from dotenv import load_dotenv
load_dotenv()
 
redis_broker = os.environ['REDIS_BROKER']
redis_backend = os.environ['REDIS_BACKEND']
app = Celery('tasks', broker=redis_broker,  backend=redis_backend)

@app.task
def sub(x, y):
    return x-y