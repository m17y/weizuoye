# -*- coding:utf-8 -*-

import time
from celery import Task
from init_celery import celery
import redis
from logic import jgsend

r = redis.StrictRedis(host='localhost', port=6379, db=0)
class BaseTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print 'task done: {0}'.format(retval)
        return super(BaseTask, self).on_success(retval, task_id, args, kwargs)
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print 'task fail, reason: {0}'.format(exc)
        return super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@celery.task()
def sendmail(mail,b):
    print('sending mail to %s...' % mail)
    print(b)

@celery.task()
def send_course_task(from_user,users,cousertask):
    print 'from_user',from_user
    print 'users',users
    print 'cousertask',cousertask
    # r.publish(cousertask.courseid, cousertask)
    try:
        jgsend.audience(registration_id=users)
        for u in users:
            message = Message()
            message.course_task = course_task
            message.course = ObjecyId(cousertask.courseid)
            message.from_user = from_user
            message.user = ObjecyId(u)
            message.content = course.name+','+cousertask.content
            message.save()
    except Exception as e:
        pass



# a = send_course_task.apply_async(args=[{'to':2},'2'])

#发布端的代码
# r.publish('spub', input) 
# 订阅
# p = r.pubsub()  
# p.subscribe('excelFile')  
# for item in p.listen():      
#     print item  
#     if item['type'] == 'message':    
#         data =item['data']   
#         r.set('s',32)  
#         print data  
#         if item['data']=='over':  
#             break;  
# p.unsubscribe('spub')  
# print '取消订阅'  

