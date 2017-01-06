
# gunicorn
gunicorn -b 0.0.0.0:8000 --workers=2 --log-file error.log wsgi:application&

gunicorn --worker-class=gevent wsgi:application