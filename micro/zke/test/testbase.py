# -*- coding:utf-8 -*-

HOST = 'http://localhost:9878'
import json
import urllib
import urllib2
import cookielib

def get_cookie_opener(path):
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load(path, ignore_discard=True, ignore_expires=True)
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie','cookiename=cookievalue'))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    return opener

def get_requese_data(values,URL,method,cookie='cookie.txt'):
    values = urllib.urlencode(values)
    opener = get_cookie_opener(cookie)
    req = urllib2.Request(url = URL,data=values)
    req.get_method = lambda: method
    response = opener.open(req)
    data = json.loads(response.read())
    return data

TEST_INDEX = []
def utest(num):
    global TEST_INDEX
    def decorator(func):
        def wrapper(*args, **kw):
            TEST_INDEX.insert(num,func.__name__)
            # print '%s %s():' % (num, func.__name__)
            print TEST_INDEX
        return wrapper
    return decorator