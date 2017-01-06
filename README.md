## djcelery
    This is for djcelery,djcelery is celery integration for Django. 

### celery
    task(django or others ) -> broker(redis) -> worker(celery) -> backend(redis)

### ENV
    python==2.7.13
    Django==1.8
    celery==3.1.18
    django-celery==3.1.16
    redis_version==3.0.4
    
### settings.py
    add the celery configuration

### celery.py
    for celery
