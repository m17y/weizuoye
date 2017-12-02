# -*- coding:utf-8 -*-
import time
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class SignInHandler(BaseHandler):
    """
        此功能主要用做签到，拟采用gps定位，或者类似微信生成二维码形式来签到，或采用wifi热点开启，用户后台搜索上则签到成功
    """
    def get(self):
        courseid = self.get_argument('courseid')
        sign_in = SignIn.objects(course=ObjectId(courseid),is_close=False)
        self.write(dict(sign_in = sign_in.to_json()))

    def post(self):
        #教师创建一次签到
        courseid = self.get_argument('courseid')
        course_ssid = self.get_argument('course_ssid')
        sign_in = SignIn()
        sign_in.ts=time.time()
        sign_in.course=ObjectId(courseid)
        sign_in.course_ssid = course_ssid
        sign_in.save()
        self.write(dict(status=True,msg='add course call success'))

    def delete(self):
        userid = self.uid
        sign_in_id = self.get_argument('_id')
        ts = self.get_argument('ts')
        SignIn.objects(taskerid=ObjectId(sign_in_id)).delete()
        self.write(dict(status=True,msg='删除成功'))

    def put(self):
        #用户签到
        #TODO 签到方法，此处有待完善，数据库设计有需要修改的地方
        sign_in_id = self.get_argument('_id')
        wifi_ssid = self.get_argument('wifi_ssid')
        sign_in = SignIn.objects(id=ObjectId(sign_in_id),is_close=False).first()
        if sign_in.id == ObjectId(sign_in_id) and wifi_ssid = = sign_in.wifi_ssid:
            SignIn.objects(id=ObjectId(sign_in_id)).update_one(push__users=self.user)
        if True:
            SignIn.objects(courseid=courseid,classesid=classesid).update_one(push__users=self.user)
            self.write(dict(status=True,msg=' success'))
        else:
            self.write(dict(status=True,msg=' fail'))

