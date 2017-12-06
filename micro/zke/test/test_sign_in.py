# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import unittest
import cookielib
from testbase import*
HOST = 'http://localhost:9878'

SSID = 'test'

class TestSignIn(unittest.TestCase):


    """
    使用Python自带的unittest模块，编写用户签到模块
    """
    def test_get_signin(self):
        print '获得最近课程的签到列表'
        pass

    def test_creat_signin(self):
        print '创建一次课程签到'
        URL = HOST+'/course/signin'
        values={
            'courseid':'5a27ff69b4d0131d3bb8deac',
            'signkey':SSID,
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        req.get_method = lambda: 'POST'
        response = opener.open(req)
        data = json.loads(response.read())
        global SIGNIN
        SIGNIN = data.get('sign_in')
        print SIGNIN
        self.assertEquals(data.get('status',''),True)

    def test_put_signin(self):
        print '学生答到测试...'
        URL = HOST+'/course/signin'
        values={
            '_id':SIGNIN,
            'signkey':SSID,
        }
        print SIGNIN

        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        req.get_method = lambda: 'POST'
        response = opener.open(req)
        data = json.loads(response.read())
        self.assertEquals(data.get('status',''),True)

    def test_put_signin(self):
        print '学生答到测试...'
        URL = HOST+'/course/signin'
        values={
            '_id':SIGNIN,
            'signkey':SSID,
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        req.get_method = lambda: 'PUT'
        response = opener.open(req)
        data = json.loads(response.read())
        self.assertEquals(data.get('status',''),True)

    def test_del_signin(self):
        print '删除签到'
        URL = HOST+'/course/signin'
        values={
            '_id':SIGNIN,
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        req.get_method = lambda: 'DELETE'
        response = opener.open(req)
        data = json.loads(response.read())
        self.assertEquals(data.get('status',''),True)

if __name__ == '__main__': 
    #TODO做一个装饰器用来确定执行顺序
    suite = unittest.TestSuite()  
    suite.addTest(TestSignIn('test_get_signin'))  
    suite.addTest(TestSignIn('test_creat_signin'))  
    suite.addTest(TestSignIn('test_put_signin'))  
    suite.addTest(TestSignIn('test_del_signin'))  
    
  
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    unittest.TextTestRunner(verbosity=2).run(suite)  