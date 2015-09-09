# Server Info #

##This server use Flask+uWSGI+Nginx on python3.4 Linux.##

### Environment Require: ###
- `python3 -m pip install flask pytesseract uwsgi`
- `apt-get install tesseract nginx`

### Configure ###
As you can see,uWSGI could use *.ini file to config.
1. Under localhost, use `uwsgiRunLocalTest.sh` to test *Client<---->uWSGI<-->Flask*
2. When use formally, use `uwsgiRunServer.sh` to provide a UNIX socket in  system's   */tmp/uwsgi.sock* 

After uWSGI's configuration, Next is Nginx.
1. if use [LNMP Package](http://lnmp.org/) ,just put `api.5pipi.tk.conf` to your nginx's Vhost folder.
2. Change its content to yourselves.
3. Restart Nginx,and Try  to view the site.


### Reference ###
- [http://www.jianshu.com/p/e6ff4a28ab5a](http://www.jianshu.com/p/e6ff4a28ab5a "基于nginx和uWSGI在Ubuntu上部署Django")
- [http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html "Setting up Django and your web server with uWSGI and nginx — uWSGI 2.0 documentation")
- [http://docs.jinkan.org/docs/flask/deploying/uwsgi.html](http://docs.jinkan.org/docs/flask/deploying/uwsgi.html "uWSGI — Flask 0.10.1 文档")
- [Google](https://www.google.com/?gws_rd=cr,ssl "Gooooooooooooogle")

![Hello,Google~](https://www.google.com.hk/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png)