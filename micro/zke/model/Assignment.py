# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
from bson import ObjectId
import datetime,time
from mongoengine import *
from Base import connect,BaseObject

# connect('mydb')

class User(Document,BaseObject):
    """用户类"""
    count = property(lambda self: self.usercount())
    profile_name = StringField(max_length=30,unique=True)
    tel = IntField(max_length=11, min_length=11)
    nickname = StringField(max_length=30)
    name = StringField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    is_teacher = BooleanField(default=False)
    # course = ListField(ReferenceField(Course,reverse_delete_rule=PULL))
    # owncourse = ListField(ReferenceField(Course,reverse_delete_rule=PULL))
    def unique_save(self):
        if not self.count:
            self.save()
            return True,'successs'
        else:
            return False,'fail'

    def usercount(self):
        user_count = User.objects(name=self.name).count()
        return user_count

class Course(Document,BaseObject):
    """课程类"""
    course_type = StringField(max_length=30)
    name = StringField(max_length=30)
    code = StringField(max_length=30,unique=True)
    owner = ObjectIdField()
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))


class School(Document,BaseObject):
    """学校类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    description = StringField()

class College(Document,BaseObject):
    """学院类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    school = ReferenceField(School, reverse_delete_rule=CASCADE)

# class CourseUser(Document):
#     """课程类"""
#     course = ReferenceField(Course, reverse_delete_rule=CASCADE)
#     owner = ReferenceField(User, reverse_delete_rule=CASCADE)
#     users = ListField(ReferenceField(User,reverse_delete_rule=PULL))


class CourseTask(Document,BaseObject):
    """课程习题类"""
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    owner = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=30)
    finish_user = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    is_close = BooleanField(default=False)
    fid = ListField()
    ts = FloatField()


class SignIn(Document,BaseObject):
    """签到"""
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    ts = FloatField()
    signkey = StringField(max_length=10,required=False)
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    is_close = BooleanField(default=False)

class Task(Document,BaseObject):
    """作业类"""
    course_task = ReferenceField(CourseTask, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=10,required=False)
    fid = ListField()
    is_finish = BooleanField(default=False)

class Message(Document,BaseObject):
    """消息类"""
    course_task = ReferenceField(CourseTask, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    form_user = ReferenceField(User, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=10,required=False)
    is_read = BooleanField(default=False)

if __name__ == '__main__':
    # 初始化
    user = User()
    user.name='Root'
    user.profile_name = 'success'
    import hashlib
    user.password = hashlib.md5('111111').hexdigest()
    user.save()

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
    cs.users = [user]
    cs.owner = user.id

    ct = CourseTask()
    ct.course = cs
    ct.owner = user
    task = Task()
    task.course_task = ct
    task.user = user
    task.content = '000000'
    cs.save()
    sc.save()
    cg.save()
    ct.save()
    task.save()
    import pdb; pdb.set_trace()
    from bson import ObjectId
    coursesids = [ObjectId('5a2cd4dcb4d013121bb1e24a'),ObjectId("5a2cd433b4d013115b6ccebe")]
    coursetask=CourseTask.objects(course__in=coursesids).distinct('finish_user')
# 删除依赖
# User.objects(name="Root").delete()
