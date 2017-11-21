# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from model import Assignment as ag
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class SchoolAddHandler(BaseHandler):

    def post(self):
        bm = ag.School()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))

@needcheck()
class SchoolDelHandler(BaseHandler):
    def post(self):
        pass

@needcheck()
class CollegeClassAddHandler(BaseHandler):

    def post(self):
        bm = ag.CollegeClass()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))

@needcheck()
class CollegeAddHandler(BaseHandler):

    def post(self):
        bm = ag.College()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))
