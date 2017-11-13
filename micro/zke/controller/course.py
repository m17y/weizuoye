# -*- coding:utf-8 -*-
import time
import hashlib
from bson import ObjectId
import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *


@needcheck()
class CourseTaskAddHandler(BaseHandler):
    def post(self):
        if self.user['is_teacher']:
            courseid = self.get_argument('courseid')
            classesid = self.get_argument('classesid')
            task = {
                'title':self.get_argument('title'),
                'context':self.get_argument('context'),
                'videoid':self.get_argument('videoid'),
                'ts':time.time(),
                'taskid':ObjectId()
            }
            if CourseTask.objects(classesid=classesid).count():
                CourseTask.objects(courseid=courseid,classesid=classesid).update_one(push__task=task)
            else:
                ct = CourseTask()
                ct.courseid = courseid
                ct.classesid = classesid
                ct.task = [task]
                ct.save()
        self.write(dict(status=True,msg='msg'))

    def delete(self):
        if self.is_teacher:
            courseid = self.get_argument('courseid')
            classesid = self.get_argument('classesid')
            title = self.get_argument('title')
            context = self.get_argument('context')
            videoid = self.get_argument('videoid')
            ct = CourseTask
            ct.courseid = courseid
            ct.classesid = classesid
            ct.task = [{'title':title,'context':context,'videoid':videoid}]
            ct.save()
            Page.objects(id='...').update_one(push__authors=john)
        self.write(dict(status=status,msg=msg))