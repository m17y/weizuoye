# -*- coding: utf-8 -*-
'''
Created on 2016年6月11日

@author: Su
'''
import time
from mongoengine import *

connect('weizuoye', host='127.0.0.1', port=27017)

connect('teacher', alias='db-teacher',host='127.0.0.1', port=27017)


class BaseObject(object):
    update_time = time.time()
    # meta = {'allow_inheritance': True}
    def modelfactory(self,args):
        for k ,v in args.items():
            try:
                self[k] = v
            except Exception as e:
                pass
