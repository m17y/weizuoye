# -*- coding:utf-8 -*-
import time
import json
import hashlib
from bson import ObjectId
import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *
from tasks.task_server import *
# @needcheck()
class CourseHandler(BaseHandler):
    """docstring for CourseHandler"""

    def get(self):
        #获得用户课程信息
        profile_name = self.get_argument('profile_name')
        user = User.objects(profile_name=profile_name).first()
        tag = self.get_argument('tag','')
        if tag == 'ain':
            courses=Course.objects(owner=user.id).all()
            coursetask=CourseTask.objects(course__in=courses,is_close=False)
            ct_map = {}
            coursetask = json.loads(coursetask.to_json())
            for ct in coursetask:
                ct_map.setdefault(ct['course']['$oid'],0)
                ct_map[ct['course']['$oid']]+=len(ct['finish_user'])
            courses = json.loads(courses.to_json())
            for course in courses:
                course['unfinish']=ct_map.get(course['_id']['$oid'])
            self.write(dict(courses=courses))
            return
        if tag== 'follower':

            # courses=Course.objects(id__in=[user])
            # self.write(dict(courses=courses.to_json()))
            return

    def post(self):
        #添加一个课程
        code = self.get_argument('code')
        name = self.get_argument('name')
        course_type = self.get_argument('course_type')
        course = Course()
        course.owner = self.user
        course.name = name
        course.course_type = course_type
        course.save()

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
        Course.objects(id=ObjectId(courseid)).delete()
        self.write(dict(status=True,msg='del success'));return


class CourseJoinHandler(BaseHandler):
    #加入一个课程
    def post(self):
        code = self.get_argument('code')
        Course.objects(code=code).update_one(push__users=self.user)
        self.write(dict(status=True,msg='msg',course=str(course.id)))

class CourseAppear(object):
    #退出一个课程
    def post(self):
        courseid = self.get_argument('_id')
        Course.objects(id=self.id).update_one(pull__users=self.user)
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
        #获取课程所有的用户
        courseid = self.get_argument('courseid')
        course = Course.objects(id=ObjectId(courseid)).first()
        users = course.user
        self.write(dict(users=users.to_json(),status=True))

@needcheck()
class CrouseTaskStatus(BaseHandler):
    def post(self,courseid):
        #获取课程所有用户的作业完成情况
        course_taskid = self.get_argument('course_taskid','')
        if not course_taskid:
            course = Course.objects(id=ObjectId(courseid)).first()
            users = course.user
            self.write(dict(users=users.to_json(),status=True))

