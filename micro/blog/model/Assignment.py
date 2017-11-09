# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
import datetime
from mongoengine import *
from BaseMongodb import connect
# connect('mydb')

class BaseMo(Document):
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'allow_inheritance': True}
    def modelfactory(self,args):
        for k ,v in args.items():
            try:
                self[k] = v
            except Exception as e:
                pass

class User(BaseMo):
    """用户类"""
    name = StringField(max_length=30)
    identity =  IntField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    class_level=IntField()
    classid = StringField(max_length=30)
    is_teacher = BooleanField(default=False)
    course = ListField()
    # course = ReferenceField(Course, reverse_delete_rule=PULL)
    school = StringField(max_length=30)
    college = StringField(max_length=30)
    def login_verfiy(self):
        user = User.objects(name=self.name).first()
        if user and user.password==self.password:
            return True,'successs'
        else:
            return False,'fail'
    @property
    def usercount(self):
        user_count = User.objects(name=self.name).count()
        return user_count

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
    task = ListField()

class School(Document):
    """学校类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)

class CollegeClass(Document):
    """学院班级类"""
    name = StringField(max_length=30)

class College(Document):
    """学院类"""
    name = StringField(max_length=30)
    code = StringField(max_length=30)
    school = ReferenceField(School, reverse_delete_rule=PULL)

class task(Document):
    """作业类"""
    courseid = StringField(max_length=20,required=False)
    taskerid = DateTimeField(default=datetime.datetime.utcnow)
    userid = StringField(max_length=10,required=False)
    content = StringField(max_length=10,required=False)

if __name__ == '__main__':
    # cg = ClassGroup()
    # cg.num = '001'
    # cg.name = '软件工程系'
    # cg.save()
    import pdb;pdb.set_trace()
    st = Student()
    st.name='suyf'
    st.classgroup = cg
    st.ver
    st.save()
    # st = Student.objects(name='suyf')
    # st.classgroup = cg

    # import pdb;pdb.set_trace()