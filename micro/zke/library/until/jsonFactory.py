# -*- coding: utf-8 -*-
'''
Created on 2016年6月12日

@author: Su
'''
import json
class MyJson:
    def __init__(self, **entries): 
        self.__dict__.update(entries)