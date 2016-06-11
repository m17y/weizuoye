# -*- coding: utf-8 -*-
'''
Created on 2016年6月11日

@author: Su
'''
import settings
import pymongo
class BaseMongodb():
    def __init__(self):
        print settings.options.mongo
        conn  = pymongo.Connection(
            host=settings.options.mongo
            )
        self.db = conn.workonline