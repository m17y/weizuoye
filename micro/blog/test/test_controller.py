# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import unittest

HOST = 'http://localhost:9878'

class TestReg(unittest.TestCase):
    """
    使用Python自带的unittest模块，编写sort.py测试用例
    """

    # def test_get_reg(self):
    #     URL = HOST+'/login'
    #     req = urllib2.Request(URL)
    #     response = urllib2.urlopen(req)
    #     data = response.read()

    # def test_post_reg(self):
    #     values={
    #     'name':'suyf',
    #     'password':'111111'
    #     }
    #     URL = HOST+'/login'
    #     values = urllib.urlencode(values)
    #     req = urllib2.Request(url = URL,data =values)
    #     response = urllib2.urlopen(req)
    #     data = json.loads(response.read())
    #     print data
    #     self.assertEquals(data.get('status',''),True)

    def test_task(self):
        URL = HOST+'/coursetask'
        values={
        'courseid':'courseid',
        'classesid':'classesid',
        'title':'title',
        'context':'context',
        'videoid':'videoid'
        }
        values = urllib.urlencode(values)
        req = urllib2.Request(url = URL,data =values)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
        print data
        self.assertEquals(data.get('status',''),True)


if __name__ == '__main__':  
    unittest.main()