# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import unittest
import cookielib
from testbase import*
HOST = 'http://localhost:9878'
class TestReg(unittest.TestCase):
    """
    使用Python自带的unittest模块，编写sort.py测试用例
    """
    def test_get_users(self):
        print 'BeginTest:test_get_users.....'
        URL = HOST+'/user'
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL)
        response = opener.open(req)
        data = json.loads(response.read())
        print data['data']
        self.assertEquals(data.get('status',''),True)

    def test_post_users(self):
        print 'BeginTest:test_post_users.....'
        URL = HOST+'/user'
        values={
            'name':'suyf22',
            'password':'111111',
            'email':'suyf@qq.com',
            'nickname':'suyf',
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        response = opener.open(req)
        data = json.loads(response.read())
        print data
        self.assertEquals(data.get('status',''),True)

    def test_put_users(self):
        print 'BeginTest:test_put_users.....'
        URL = HOST+'/user'
        values={
            'email':'putsuyf@qq.com',
            'nickname':'putsuyf',
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        req.get_method = lambda: 'POST'
        response = opener.open(req)
        data = json.loads(response.read())
        self.assertEquals(data.get('status',''),True)

    # def test_delete_users(self):
    #     print 'BeginTest:test_put_users.....'
    #     URL = HOST+'/users'
    #     values={
    #         'uid':'xxx',
    #     }

    #     values = urllib.urlencode(values)
    #     opener = get_cookie_opener('cookie.txt')
    #     req = urllib2.Request(url = URL,data=values)
    #     req.get_method = lambda: 'DELETE'
    #     response = opener.open(req)
    #     data = json.loads(response.read())
    #     self.assertEquals(data.get('status',''),True)

if __name__ == '__main__':  
    unittest.main()