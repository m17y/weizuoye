# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
import datetime,time
from mongoengine import *
from Base import connect,BaseObject
# connect('mydb')

class Course(Document):
    """课程类"""
    course_type = StringField(max_length=30)
    name = StringField(max_length=30)
    code = StringField(max_length=30)


class User(Document,BaseObject):
    """用户类"""
    count = property(lambda self: self.usercount())

    nickname = StringField(max_length=30)
    name = StringField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    is_teacher = BooleanField(default=False)
    course = ListField(ReferenceField(Course,reverse_delete_rule=PULL))

    def unique_save(self):
        if not self.count:
            self.save()
            return True,'successs'
        else:
            return False,'fail'

    def usercount(self):
        user_count = User.objects(name=self.name).count()
        return user_count

class School(Document):
    """学校类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    description = StringField()

class College(Document):
    """学院类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    school = ReferenceField(School, reverse_delete_rule=CASCADE)

# class CourseUser(Document):
#     """课程类"""
#     course = ReferenceField(Course, reverse_delete_rule=CASCADE)
#     owner = ReferenceField(User, reverse_delete_rule=CASCADE)
#     users = ListField(ReferenceField(User,reverse_delete_rule=PULL))

class Course(Document):
    """课程类"""
    course_type = StringField(max_length=30)
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    owner = ReferenceField(User, reverse_delete_rule=CASCADE)
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))

class CourseTask(Document):
    """课程习题类"""
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    owner = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=30)
    fid = ListField()
    ts = FloatField()

class SignIn(Document):
    """签到"""
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    ts = FloatField()
    wifi_ssid = StringField(max_length=10,required=False)
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    is_close = BooleanField(default=False)

class Task(Document):
    """作业类"""
    course_task = ReferenceField(CourseTask, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=10,required=False)
    fid = ListField()
    is_finish = BooleanField(default=False)

class Message(Document):
    """消息类"""
    course_task = ReferenceField(CourseTask, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    form_user = ReferenceField(User, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=10,required=False)
    is_read = BooleanField(default=False)

if __name__ == '__main__':
    # 初始化
    import pdb;pdb.set_trace()
    user = User()
    user.name='Root'
    sc =School()
    sc.name='河南大学'
    sc.code='Henu'
    sc.description='河南大学'

    cg = College()
    cg.name='软件学院'
    cg.code='Henu-001'
    cg.school = sc

    cs = Course()
    cs.course_type = '高等数学'
    cs.name = '高等数学'
    cs.code = 'math'
    cs.owner = user
    ct = CourseTask()
    ct.course = cs
    ct.owner = user
    task = Task()
    task.course_task = ct
    task.user = user
    task.content = '000000'
    sc.save()
    user.save()
    cg.save()
    cs.save()
    ct.save()
    task.save()

# 删除依赖
# User.objects(name="Root").delete()
