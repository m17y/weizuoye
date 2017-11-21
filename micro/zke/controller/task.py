# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class CourseTaskHandler(BaseHandler):

    def get(self):
        course_task = self.get_argument('course_task')
        data = Task.objects(user=ObjectId(self.uid),course_task=ObjectId(course_task))[0:5]
        self.write(dict(data=data.to_json(),status=True,msg='xxx'))

    def post(self):
        bm = ag.School()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.unique_save()
        self.write(dict(status=status,msg=msg))

    def delete(self):
        userid = self.uid
        taskerid = self.get_argument('taskerid')
        Task.objects(taskerid="taskerid",userid=userid).delete()
        self.write(dict(status=True,msg='删除成功'))

    def put(self):
        userid = self.uid
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        taskerid = kwargs.pop('taskerid','')
        Task.objects().modify(taskerid="taskerid",userid=userid,**kwargs)
        self.write(dict(status=True,msg='modify success'))

@needcheck()
class ListTaskHndler(object):
    """docstring for UserTaskHndler"""
    def get(self):
        unfinished_task = Task.objects(user=self.uid,is_finish=False)
        self.write(dict(data=unfinished_task.to_json(),status=True,msg='xxx'))
