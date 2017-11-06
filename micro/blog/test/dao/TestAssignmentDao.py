# -*- coding: utf-8 -*-
'''
Created on 2016年6月11日

@author: Su
'''
from dao.mongo.AssignmentDao import AssignmentDao
import unittest
class TestAssignments(unittest.TestCase):
    def test_create_local_auth(self):
        email = "test"
        name = "name"
        hashed_password = "hashed_password"
        asgdao = AssignmentDao()
        asgdao.create_local_auth(hashed_password, email, name)

if __name__ == '__main__':
    unittest.main()
