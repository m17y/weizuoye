# -*- coding: utf-8 -*-
'''
Created on 2016年6月11日

@author: Su
'''
from mongoengine import *

connect('weizuoye', host='127.0.0.1', port=27017)

connect('teacher', alias='db-teacher',host='127.0.0.1', port=27017)

