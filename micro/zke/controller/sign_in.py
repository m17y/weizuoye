# -*- coding:utf-8 -*-
import time
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import AccessHandler
from logic.access import *



@needcheck()
class SignInHandler(AccessHandler):
    """
        此功能主要用做签到，拟采用gps定位，或者类似微信生成二维码形式来签到，或采用wifi热点开启，用户后台搜索上则签到成功
    """
    def get(self):
        courseid = self.get_json_argument('courseid')
        sign_in = SignIn.objects(course=ObjectId(courseid),is_close=False)
        self.write(dict(sign_in = sign_in.to_json()))

    def post(self):
        #教师创建一次签到
        courseid = self.get_json_argument('courseid')
        signkey = self.get_json_argument('signkey')
        sign_in = SignIn()
        sign_in.ts=time.time()
        sign_in.course=ObjectId(courseid)
        sign_in.signkey = signkey
        sign_in.save()
        self.write(dict(status=True,msg='add course call success',sign_in=str(sign_in.id)))

    def delete(self):
        userid = self.uid
        sign_in_id = self.get_json_argument('_id')
        print sign_in_id
        SignIn.objects(id=ObjectId(sign_in_id)).delete()
        self.write(dict(status=True,msg='删除成功'))

    def put(self):
        #用户签到
        #TODO 签到方法，此处有待完善，数据库设计有需要修改的地方
        sign_in_id = self.get_json_argument('_id')
        signkey = self.get_json_argument('signkey')
        sign_in = SignIn.objects(id=ObjectId(sign_in_id),is_close=False).first()
        if sign_in.id == ObjectId(sign_in_id) and signkey == sign_in.signkey:
            SignIn.objects(id=ObjectId(sign_in_id)).update_one(push__users=self.user)
            self.write(dict(status=True,msg=' success'))
        else:
            self.write(dict(status=False,msg=' fail'))

