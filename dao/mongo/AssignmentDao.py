# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
from mongo.BaseMongodb import BaseMongodb

class AssignmentDao(BaseMongodb):
    def __init__(self, session=None):
        BaseMongodb.__init__(self)
        pass
    def create_local_auth(self,password,email,name):
        print "yyy"
        self.db.local_user.insert({"password":password,"email":email,"name":name})
    def find_byid(self):
        pass
    