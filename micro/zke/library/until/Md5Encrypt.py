# -*- coding: utf-8 -*-
'''
Created on 2016年6月11日

@author: Su
'''
import base64
import hashlib
KEY = "suyf19940117"
def date_encrypt(value):
    base64_str = base64.b64encode(value)
    md5 = hashlib.md5()
    md5.update(base64_str+value)
    md5_str = md5.hexdigest()
    return md5_str
if __name__ == "__main__":
    md5_str = date_encrypt("suyf")
    print md5_str