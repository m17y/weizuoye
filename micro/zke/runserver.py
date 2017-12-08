# -*- coding: utf-8 -*-
'''
Created on 2016-6-10

@author: Administrator
'''
import os
import tornado.options
import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
from url import Application
from setting import options

class SetApplication(Application):
    def __init__(self):
        settings = dict(
            blog_title=u"Tornado Blog",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # ui_modules={"Entry": EntryModule},
            # xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        super(Application, self).__init__(self.handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(SetApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    print 'listen on :'+str(options.port)
    main()