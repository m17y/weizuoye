# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
import datetime,time
from mongoengine import *
from Base import connect,BaseObject
# connect('mydb')



class User(Document,BaseObject):
    """用户类"""
    count = property(lambda self: self.usercount())

    nickname = StringField(max_length=30)
    name = StringField(max_length=30)
    identity =  IntField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    class_level=IntField()
    classid = StringField(max_length=30)
    is_teacher = BooleanField(default=False)
    course = ListField(ReferenceField(Course,reverse_delete_rule=PULL))
    # course = ReferenceField(Course, reverse_delete_rule=PULL)
    school = StringField(max_length=30)
    college = StringField(max_length=30)

    def unique_save(self):
        if not self.count:
            self.save()
            return True,'successs'
        else:
            return False,'fail'

    @property
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

class CourseType(Document):
    """学科类，按学科分类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    college = StringField(max_length=30)

class Course(Document):
    """课程类"""
    course_type = StringField(max_length=30)
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    owner = ReferenceField(User, reverse_delete_rule=CASCADE)
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))

class CollegeClass(Document):
    """学院班级类"""
    count = property(lambda self: self.usercount())

    name = StringField(max_length=30)
    college = ReferenceField(College, reverse_delete_rule=CASCADE)
    school = ReferenceField(School, reverse_delete_rule=CASCADE)
    courses = ListField(ReferenceField(Course,reverse_delete_rule=PULL))
    users = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    def unique_save(self):
        if not self.count:
            self.save()
            return True,'successs'
        else:
            return False,'fail'
    @property
    def collegeclass_count(self):
        user_count = CollegeClass.objects(name=self.name).count()
        return user_count


class CourseTask(Document):
    """课程习题类"""
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    collegeclass = ReferenceField(CollegeClass, reverse_delete_rule=CASCADE)
    owner = ReferenceField(User, reverse_delete_rule=CASCADE)
    tasks = ListField()


class Task(Document):
    """作业类"""
    course_task = ReferenceField(CourseTask, reverse_delete_rule=CASCADE)
    taskerid = StringField(max_length=10,required=False)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=10,required=False)

if __name__ == '__main__':
    # 初始化
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

    collegc = CollegeClass()
    collegc.name='1'
    collegc.college = cg
    collegc.school = sc

    cs = Course()
    cs.course_type = '高等数学'
    cs.name = '高等数学'
    cs.code = 'math'
    cs.owner = user
    cs.classes = [collegc]
    ct = CourseTask()
    ct.course = cs
    ct.collegeclass = collegc
    ct.owner = user
    task = Task()
    task.course_task = ct
    task.user = user
    task.taskerid = '000000'
    sc.save()
    user.save()
    cg.save()
    collegc.save()
    cs.save()
    ct.save()
    task.save()

# 删除依赖
# User.objects(name="Root").delete()
