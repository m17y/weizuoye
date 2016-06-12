# -*- coding: utf-8 -*-
'''
Created on 2016年6月12日

@author: Su
'''
class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

if __name__ == "__main__":
    args = {'a': 1, 'b': 2}
    s = Struct(**args)
    print s.a