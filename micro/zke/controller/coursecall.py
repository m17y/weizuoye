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
class CourseCallHandler(BaseHandler):
    """
        此功能主要用做签到，拟采用gps定位，或者类似微信生成二维码形式来签到，或采用wifi热点开启，用户后台搜索上则签到成功
    """
    def get(self):
        pass

    def post(self):
        courseid = self.get_argument('courseid')
        course = CourseCall.objects(course=ObjectId(courseid)).first()
        ts = time.time()
        coursecall = CourseCall()
        coursecall.ts=ts
        coursecall.course=course
        coursecall.save()
        self.write(dict(status=True,msg='add course call success'))

    def delete(self):
        userid = self.uid
        coursecall_id = self.get_argument('_id')
        ts = self.get_argument('ts')
        CourseCall.objects(taskerid=ObjectId(coursecall_id),ts=float(ts)).delete()
        self.write(dict(status=True,msg='删除成功'))

    def put(self):
        #TODO 签到方法，此处有待完善，数据库设计有需要修改的地方
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        if True:
            CourseCall.objects(courseid=courseid,classesid=classesid).update_one(push__users=self.user)
            self.write(dict(status=True,msg=' success'))
        else:
            self.write(dict(status=True,msg=' fail'))

