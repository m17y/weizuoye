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
            self.write(dict(courses=courses.to_json()))
            return
        else:
            coursesids = self.user['course']
            courses=Course.objects(id__in=coursesids)
            self.write(dict(courses=courses.to_json()))
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
        coursetaskid = self.get_argument('coursetaskid')
        coursetask=CourseTask.objects(id=ObjectId(coursetaskid)).first()
        self.write(dict(coursetask=coursetask.to_json()))

    def post(self):
        if self.user['is_teacher']:
            courseid = self.get_argument('courseid')
            fid = self.get_argument('fid','').split(',')
            task = self.get_argument('task','')
            coursetask = CourseTask()
            coursetask.courseid = courseid
            coursetask.fid = fid
            coursetask.task = task
            coursetask.ts = time.time()
            coursetask.save()
        self.write(dict(status=True,msg='msg'))
    def put(self):
        coursetaskid = self.get_argument('coursetaskid')
        fid = self.get_argument('fid','').split(',')
        task = self.get_argument('task','')
        CourseTask.objects().modify(id=ObjectId(coursetaskid),**{'fid':fid,'task':task})
        self.write(dict(status=True,msg='modify success'))

    def delete(self):
        if self.is_teacher:
            courseid = self.get_argument('courseid')
            #TODO删除fid（文件）
            CourseTask.objects(courseid=ObjectId(courseid)).delete()
        self.write(dict(status=status,msg=msg))

@needcheck()
class CrouseUserStatistic(BaseHandler):
    def post(self):
        pass
        #TODO tongjifenshudeng