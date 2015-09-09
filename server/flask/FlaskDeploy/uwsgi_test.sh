uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi

#uwsgi --ini myproject.ini