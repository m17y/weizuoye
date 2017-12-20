# -*- coding:utf-8 -*-
import time
import hashlib
from bson import ObjectId
import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *
from tasks.task_server import *
@needcheck()
class CourseHandler(BaseHandler):
    """docstring for CourseHandler"""
    def get(self):
        #获得用户课程信息
        owner = self.get_argument('_id','')
        if owner:
            courses=Course.objects(owner=ObjectId(owner))
            self.write(dict(courses=courses.to_json()))
            return
        else:
            coursesids = self.user['course']
            courses = Course.objects(id__in=coursesids)
            self.write(dict(courses=courses.to_json()))
            return

    def post(self):
        #添加用户课程(或者加入一个课程)
        ###TODO课程关联以及是否需要在用户表（course）和课程表（user）中都插入课程id或（用户id）
        code = self.get_argument('code','')
        if code:
            User.objects(code=code).update_one(push__course=ObjectId(courseid))
        else:
            code = self.get_argument('code')
            name = self.get_argument('name')
            course_type = self.get_argument('course_type')
            course = Course()
            course.owner = self.user
            course.name = name
            course.course_type = course_type
            course.save()
            # User.objects(id=ObjectId(self.uid)).update_one(push__course=course.id)
        self.write(dict(status=True,msg='msg',course=str(course.id)))

    def put(self):
        #更新用户课程
        userid = self.uid
        course = Course()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        _id = kwargs.pop('_id','')
        course.modelfactory(kwargs)
        # Course.objects(id=ObjectId(_id)).modify(**kwargs)#两个都可以
        Course.objects(id=ObjectId(_id)).update_one(**kwargs)
        self.write(dict(status=True,msg='modify success'))

    def delete(self):
        #删除用户课程
        #TODO未完成
        courseid = self.get_argument('_id')
        course=Course.objects(id=ObjectId(courseid)).first()
        if course.owner==self.user:
            Course.objects(id=ObjectId(courseid)).delete()
            self.write(dict(status=True,msg='del success'));return
        else:
            User.objects(id=self.id).update_one(pull__course=course)
            self.write(dict(status=True,msg='del success'));return


@needcheck()
class CourseTaskHandler(BaseHandler):

    def get(self):
        #获得课程习题
        coursetaskid = self.get_argument('coursetaskid')
        coursetask=CourseTask.objects(id=ObjectId(coursetaskid)).first()
        self.write(dict(coursetask=coursetask.to_json()))

    def post(self):
        #添加课程习题
        if self.user['is_teacher']:
            courseid = self.get_argument('courseid')
            fid = self.get_argument('fid','').split(',')
            content = self.get_argument('content','')
            course = Course.objects(id=ObjectId(courseid)).first()
            coursetask = CourseTask()
            coursetask.course = course
            coursetask.fid = fid
            coursetask.content = content
            coursetask.ts = time.time()
            coursetask.save()
            result = send_course_task.apply_async(args=[self.user,course.users,coursetask])
            if result == 'SUCCESS':
                self.write(dict(status=True,msg='msg'));return
            else:
                self.write(dict(status=True,msg='msg'));return
    def put(self):
        #更新课程习题
        coursetaskid = self.get_argument('coursetaskid')
        fid = self.get_argument('fid','').split(',')
        task = self.get_argument('task','')
        CourseTask.objects().modify(id=ObjectId(coursetaskid),**{'fid':fid,'task':task})
        self.write(dict(status=True,msg='modify success'))

    def delete(self):
        #删除课程习题
        if self.is_teacher:
            courseid = self.get_argument('courseid')
            #TODO删除fid（文件）
            CourseTask.objects(courseid=ObjectId(courseid)).delete()
        self.write(dict(status=status,msg=msg))

@needcheck()
class CrouseUser(BaseHandler):
    def post(self):
        #获取课程所以的用户
        courseid = self.get_argument('courseid')
        #TODO tongjifenshudeng