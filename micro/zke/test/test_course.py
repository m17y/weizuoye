# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import unittest
import cookielib
from testbase import*
HOST = 'http://localhost:9878'

UID = '5a27ff69b4d0131d3bb8deaa'
COURSEID = ''

class TestCourse(unittest.TestCase):


    """
    使用Python自带的unittest模块，编写课程测试模块
    """
    def test_1_get_course(self):
        print '获得用户课程'
        
        pass

    def test_2_creat_course(self):
        print '创建课程'
        URL = HOST+'/course'
        values={
            'name':'人工智能',
            'code':'roobt',
            'course_type':'feauter',
        }
        data = get_requese_data(values,URL,'POST')
        global COURSEID
        
        COURSEID = data.get('course')
        self.assertEquals(data.get('status',''),True)

    def test_4_put_course(self):
        print '更新课程'
        URL = HOST+'/course'
        values={
            '_id':COURSEID,
            'name':'人工智能',
            'code':'roobt',
            'course_type':'feauter2',
        }
        data = get_requese_data(values,URL,'PUT')
        self.assertEquals(data.get('status',''),True)

    def test_5_del_signin(self):
        print '删除课程'
        URL = HOST+'/course'
        values={
            '_id':COURSEID,
        }
        data = get_requese_data(values,URL,'DELETE')
        print data
        self.assertEquals(data.get('status',''),True)

if __name__ == '__main__': 

    unittest.main()
    # print TEST_INDEX
    # suite = unittest.TestSuite() 
    # for k in TEST_INDEX:
    #     suite.addTest(TestCourse(k))  
    #     print k,''
    # unittest.TextTestRunner().run(suite)