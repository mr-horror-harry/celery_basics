from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'every-minute': {
    'task': 'tasks.square',
    'schedule': crontab(minute='*/1'),
    'args': (12, ),
    },

    'every-minute': {
    'task': 'tasks.square',
    'schedule': crontab(minute='*/1'),
    'args': (12, ),
    },

    'every-minute': {
    'task': 'tasks.square',
    'schedule': crontab(minute='*/1'),
    'args': (12, ),
    },
}