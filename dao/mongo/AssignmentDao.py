# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
from mongo.BaseMongodb import BaseMongodb
import uuid
class AssignmentDao(BaseMongodb):
    def __init__(self, session=None):
        BaseMongodb.__init__(self)
        pass
    def create_local_auth(self,password,email,name):
        user_id = str("weizuoye_")+str(uuid.uuid1())
        self.db.local_user.insert({"password":password,"email":email,"name":name,"user_id":user_id})
        return user_id
    def find_by_name(self,name):
        user = self.db.local_user.find_one({"name":name})
        return user
    def find_by_email(self,email):
        user = self.db.local_user.find_one({"email":email})
        return user