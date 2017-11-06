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
class ClassGroup(Document):
    name = StringField(max_length=30)
    num = StringField(min_value=5, max_value=20)
    users = ListField(StringField(max_length=100))

class Student(Document):
    name = StringField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    classgroup = ReferenceField(ClassGroup, reverse_delete_rule=PULL)
class Teacher(Document):
    name = StringField(max_length=30)
    email = EmailField(required=False)
    password = StringField(max_length=50)
    meta = {'db_alias': 'db-teacher'}

class Subject(Document):
    name = StringField(max_length=20,required=False)
    creat_time = DateTimeField(default=datetime.datetime.utcnow)
    identifier = StringField(max_length=10,required=False)

if __name__ == '__main__':
    cg = ClassGroup()
    cg.num = '001'
    cg.name = '软件工程系'
    cg.save()

    st = Student()
    st.name='suyf'
    st.classgroup = cg
    st.save()
    # st = Student.objects(name='suyf')
    # st.classgroup = cg

    # import pdb;pdb.set_trace()