# -*- coding:utf-8 -*-
import time
import json
import hashlib
from bson import ObjectId
import tornado.web
from model.Assignment import *
from logic.access import *
from base import AccessHandler
from logic.access import *
from tasks.task_server import *
# @needcheck()
class CourseHandler(AccessHandler):
    """docstring for CourseHandler"""
    def get(self):
        #获得用户课程信息
        profile_name = self.get_json_argument('profile_name',self.user.profile_name)
        user = User.objects(profile_name=profile_name).first()
        tag = self.get_json_argument('tag','ain')
        if tag == 'ain':
            courses=Course.objects(owner=user.id).all()
            coursetask=CourseTask.objects(course__in=courses,is_close=False)
            ct_map = {}
            coursetask = json.loads(coursetask.to_json())
            for ct in coursetask:
                ct_map.setdefault(ct['course']['$oid'],0)
                ct_map[ct['course']['$oid']]+=len(ct['un_finish_user'])
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
        code = self.get_json_argument('code')
        name = self.get_json_argument('name')
        description = self.get_json_argument('description','')
        course_type = self.get_json_argument('course_type',name)
        course = Course()
        course.owner = self.user
        course.name = name
        course.course_type = course_type
        course.code = code
        course.description = description
        course.save()
        self.write(dict(status=True,msg='msg',course=str(course.id)))

    def put(self):
        #更新用户课程
        userid = self.uid
        course = Course()
        kwargs = dict((k,v)for k ,v in self.get_json_arguments().items())
        _id = kwargs.pop('_id','')
        course.modelfactory(kwargs)
        # Course.objects(id=ObjectId(_id)).modify(**kwargs)#两个都可以
        Course.objects(id=ObjectId(_id)).update_one(**kwargs)
        self.write(dict(status=True,msg='modify success'))

    def delete(self):
        #删除用户课程
        #TODO未完成
        courseid = self.get_json_argument('_id')
        course=Course.objects(id=ObjectId(courseid)).first()
        Course.objects(id=ObjectId(courseid)).delete()
        self.write(dict(status=True,msg='del success'));return


class CourseJoinHandler(AccessHandler):
    #加入一个课程
    def post(self):
        code = self.get_json_argument('code')
        Course.objects(code=code).update_one(push__users=self.user)
        self.write(dict(status=True,msg='msg',course=str(course.id)))

class CourseAppear(object):
    #退出一个课程
    def post(self):
        courseid = self.get_json_argument('_id')
        Course.objects(id=self.id).update_one(pull__users=self.user)
        self.write(dict(status=True,msg='del success'));return

@needcheck()
class CourseTaskHandler(AccessHandler):

    def get(self):
        #根据课程习题id获得课程习题详细内容
        coursetaskid = self.get_json_argument('coursetaskid')
        coursetask=CourseTask.objects(id=ObjectId(coursetaskid)).first()
        self.write(dict(coursetask=coursetask.to_json()))

    def post(self):
        #添加一个课程习题
        if self.user['is_teacher']:
            courseid = self.get_json_argument('courseid')
            fid = self.get_json_argument('fid','').split(',')
            content = self.get_json_argument('content','')
            course = Course.objects(id=ObjectId(courseid)).first()
            coursetask = CourseTask()
            coursetask.course = course
            coursetask.fid = fid
            coursetask.content = content
            coursetask.un_finish_user = course.users
            coursetask.ts = time.time()
            coursetask.save()
            result = send_course_task.apply_async(args=[self.user,course.users,coursetask])
            if result == 'SUCCESS':
                self.write(dict(status=True,msg='msg'));return
            else:
                self.write(dict(status=True,msg='msg'));return
    def put(self):
        #更新课程习题
        coursetaskid = self.get_json_argument('coursetaskid')
        fid = self.get_json_argument('fid','').split(',')
        task = self.get_json_argument('task','')
        CourseTask.objects().modify(id=ObjectId(coursetaskid),**{'fid':fid,'task':task})
        self.write(dict(status=True,msg='modify success'))

    def delete(self):
        #删除课程习题
        if self.is_teacher:
            courseid = self.get_json_argument('courseid')
            #TODO删除fid（文件）
            CourseTask.objects(courseid=ObjectId(courseid)).delete()
        self.write(dict(status=status,msg=msg))

@needcheck()
class CrouseUser(AccessHandler):
    def get(self):
        #获取课程所有的用户
        courseid = self.get_json_argument('courseid')
        course = Course.objects(id=ObjectId(courseid)).first()
        users = [json.loads(u.to_json()) for u in course.users]
        self.write(dict(users = users))

@needcheck()
class CrouseTaskStatus(AccessHandler):
    def get(self):
        #获取单个课程习题（or所有课程习题）的CrouseTaskStatus作业完成情况
        courseid = self.get_json_argument('courseid','')
        course_taskid = self.get_json_argument('course_taskid','')
        if courseid and not course_taskid:
            course = Course.objects(id=ObjectId(courseid),owner=self.uid).first()
            users = dict((str(u.id),u.name)for u in course.users)
            coursetask = json.loads(CourseTask.objects(course=ObjectId(courseid)).to_json())
            for ct in coursetask:
                un_finish_user=ct.get('un_finish_user',[])
                ct['un_finish_user'] = [{item['oid']:users.get(item['oid'],'')}for item in un_finish_user]
            #TODOtask里面un_finish_user
            self.write(dict(coursetask=coursetask,status=True))
        if course_taskid:
            #单个课程和多个一样
            pass

