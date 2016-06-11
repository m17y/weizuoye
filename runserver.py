# -*- coding: utf-8 -*-
'''
Created on 2016-6-10

@author: Administrator
'''
import settings
import tornado.options
import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
from web.user.url import UserApplication as ua
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ua())
    http_server.listen(settings.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()