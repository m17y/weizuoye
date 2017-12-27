# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from model import Assignment as ag
from logic.access import *
from base import AccessHandler
from logic.access import *



@needcheck()
class SchoolAddHandler(AccessHandler):

    def post(self):
        bm = ag.School()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))

@needcheck()
class SchoolDelHandler(AccessHandler):
    def post(self):
        pass

@needcheck()
class CollegeClassAddHandler(AccessHandler):

    def post(self):
        bm = ag.CollegeClass()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))

@needcheck()
class CollegeAddHandler(AccessHandler):

    def post(self):
        bm = ag.College()
        kwargs = dict((k,v[-1])for k ,v in self.requebm.arguments.items())
        bm.modelfactory(kwargs)
        status ,msg = bm.save()
        self.write(dict(status=status,msg=msg))
