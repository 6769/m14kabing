#test uwsgi service 
#uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi:app --enable-threads
#uwsgi -s /tmp/uwsgi.sock --chmod-sock=666 --module app_API_flask -callable app

#uwsgi --socket 0.0.0.0:8000 --protocol=http --wsgi-file appAPIflask.py --callable app

uwsgi --ini uwsgiConfigforLocalTest.ini
#for localtest
