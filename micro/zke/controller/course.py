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
class CourseHandler(BaseHandler):
    """docstring for CourseHandler"""

    def get(self):
        owner = self.get_argument('onwerid','')
        if owner:
            courses=Course.objects(owner=ObjectId(owner))
            self.write(dict(courses=courses.to_json(),msg='msg'))
            return
        else:
            coursesids = self.user['course']
            courses=Course.objects(id__in=coursesids)
            self.write(dict(courses=courses.to_json(),msg='msg'))
            return

    def post(self):
        code = self.get_argument('code')
        course = Course.objects(id=ObjectId(self.uid)).first()
        User.objects(id=ObjectId(self.uid)).update_one(push__course=course)
        self.write(dict(status=True,msg='msg'))

    def delete(self):
        courseid = self.get_argument('courseid')
        if self.is_teacher:
            Course.objects(owner=ObjectId(self.uid),id=ObjectId(courseid)).delete()
            self.write(dict(status=status,msg='del success'));return
        else:
            course = Course.objects(id=ObjectId(courseid)).first()
            Course.objects(courseid=courseid,classesid=classesid).update_one(pull__course=course)
            self.write(dict(status=status,msg='del success'));return

    def put(self):
        userid = self.uid
        course = Course()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        _id = kwargs.pop('_id','')
        course.modelfactory(kwargs)
        Course.objects().modify(id=ObjectId(_id),**kwargs)
        self.write(dict(status=True,msg='modify success'))


@needcheck()
class CourseTaskHandler(BaseHandler):

    def get(self):
        self.write(dict(status=True,msg='msg'))

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
        self.write(dict(status=status,msg=msg))

@needcheck()
class CrouseUserStatistic(BaseHandler):
    def post(self):
        pass
        #TODO tongjifenshudeng