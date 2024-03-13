# start redis server
redis-server

# rabbitmq
rabbitmq-server

# create rabbitmq user and password
rabbitmqctl add_user <username> <password>

rabbitmqctl set_permissions -p / <username> ".*" ".*" ".*"

rabbitmqctl list_users

# start rabbitmq celery-worker
celery -A tasks worker --loglevel=INFO

# start redis celery-worker
celery -A tasks1 worker --loglevel=INFO

# run python script
python3
>>> from tasks import square
>>> from tasks1 import sub

>>> square.delay(100)
>>> sub.delay(200, 100)

# view data in redis
redis-cli -n 1 

KEYS *

GET <key_n>