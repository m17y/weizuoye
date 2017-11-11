# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class TaskAddHandler(BaseHandler):

    def post(self):
        bm = ag.School()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))


@needcheck()
class TaskDelHandler(BaseHandler):

    def post(self):
        userid = self.uid
        taskerid = self.get_argument('taskerid')
        Task.objects(taskerid="taskerid",userid=userid).delete()
        self.write(dict(status=True,msg='删除成功'))

@needcheck()
class TaskUpdateHandler(BaseHandler):

    def post(self):
        userid = self.uid
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        taskerid = kwargs.pop('taskerid','')
        Task.objects().modify(taskerid="taskerid",userid=userid,**kwargs)
        self.write(dict(status=True,msg='删除成功'))

@needcheck()
class TaskViewHandler(BaseHandler):

    def post(self):
        print self.user
        if self.user.is_teacher:
            classid = self.get_argument('classid')
            courseid = self.get_argument('classid')
        else:
            course_task = self.get_argument('course_task')
            import pdb;pdb.set_trace()
            data = Task.objects(user=ObjectId(self.uid),course_task=ObjectId(course_task))[0:5]
            self.write(dict(data=data.to_json(),status=True,msg='xxx'))