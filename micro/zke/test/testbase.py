# -*- coding:utf-8 -*-

HOST = 'http://localhost:9878'
import json
import urllib
import urllib2
import unittest
import cookielib

def get_cookie_opener(path):
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load(path, ignore_discard=True, ignore_expires=True)
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie','cookiename=cookievalue'))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    return opener