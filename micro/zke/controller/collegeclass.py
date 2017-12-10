# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *


@needcheck()
class CollegeClassHandler(BaseHandler):
    def get(self):
        collegec_lass = self.get_argument('collegec_lass')
        data = CollegeClass.objects(id=ObjectId(collegec_lass))
        self.write(dict(data=data.to_json(),status=True,msg='xxx'))

    def post(self):
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        collegeclass = ag.CollegeClass()
        collegeclass.modelfactory(kwargs)
        status ,msg = collegeclass.unique_save()
        self.write(dict(status=status,msg='add success'))

    def delete(self):
        collegec_lass = self.get_argument('collegec_lass')
        User.objects(id=ObjectId(collegec_lass)).delete()
        self.write(dict(status=True,msg='删除成功'))

@needcheck()
class CollegeClassUserHandler(BaseHandler):
    def get(self):
        collegec_lass = self.get_argument('collegec_lass')
        data = User.objects(id=ObjectId(collegec_lass))[0:5]
        self.write(dict(data=data.to_json(),status=True,msg='xxx'))

    def delete(self):
        collegec_lass = self.get_argument('collegec_lass')
        userid = self.get_argument('userid')
        self.write(dict(status=True,msg='删除成功'))

    def post(self):
        collegec_lass = self.get_argument('collegec_lass')
        userid = self.get_argument('userid')
        self.write(dict(status=status,msg=msg))

