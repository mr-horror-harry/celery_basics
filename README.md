# init 
python3 -m venv venv

# service requirements
rabbitmq
redis

# pip requirements
amqp==5.2.0
kombu==5.3.5
python-dotenv==1.0.1
redis==5.0.3

# start redis server
redis-server

# start rabbitmq server
rabbitmq-server

# create rabbitmq user and password
rabbitmqctl add_user _username_ _password_

rabbitmqctl set_permissions -p / _username_ ".*" ".*" ".*"

rabbitmqctl list_users

# start rabbitmq celery-worker
celery -A tasks worker --loglevel=INFO

# start redis celery-worker
celery -A tasks1 worker --loglevel=INFO

# run python script
python3

from tasks import square

from tasks1 import sub

square.delay(100)

sub.delay(200, 100)

# view data in redis
redis-cli -n 1 

KEYS *

GET _key_n_