# -*- coding: utf-8 -*-
'''
Created on 2016-6-10

@author: Administrator
'''
import tornado.options
import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
from setting import SetApplication as Application
from setting import options
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()