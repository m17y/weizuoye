# -*- coding: utf-8 -*-

import jpush
import sys
sys.path.append('..')
from setting import APP_KEY,MASTER_SECRET

"""
alias：设备名称
tag:设备标签
"""
_jpush = jpush.JPush(APP_KEY, MASTER_SECRET)
_jpush.set_logging("DEBUG")

def registration(registration):
    """推送给指定的注册用户"""
    push = _jpush.create_push()
    registration = ["13065ffa4e0d53730e1"]
    push.audience = jpush.audience(
                {'registration_id':registration_id}
            )
    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print (push.payload)
    push.send()

def alias():
    push = _jpush.create_push()
    alias=["alias1", "alias2"]
    alias1={"alias": alias}
    print(alias1)
    push.audience = jpush.audience(
        jpush.tag("tag1", "tag2"),
        alias1
    )

    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print (push.payload)
    push.send()

def all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

def audience(tag=None,alias=None,registration_id=None):
    """
    选择不同audience（听众）进行推送消息
    """
    push = _jpush.create_push()
    cond = {}
    if tag and isinstance(tag,list):cond['tag'] = tag
    if alias and isinstance(alias,list):cond['tag'] = tag
    if registration_id and isinstance(registration_id,list):cond['registration_id'] = registration_id
    
    push.audience = jpush.audience(cond)
    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print (push.payload)
    push.send()


def notification():
    push = _jpush.create_push()

    push.audience = jpush.all_
    push.platform = jpush.all_

    ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1':'v1'})
    android = jpush.android(alert="Hello, Android msg", priority=1, style=1, alert_type=1,big_text='jjjjjjjjjj', extras={'k1':'v1'})

    push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)

    # pprint (push.payload)
    result = push.send()

def options():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.options = {"time_to_live":86400, "sendno":12345,"apns_production":True}
    push.send()

def platfrom_msg():
    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1':'v1'})
    android_msg = jpush.android(alert="Hello, android msg")
    push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    push.message=jpush.message("content",extras={'k2':'v2','k3':'v3'})
    push.platform = jpush.all_
    push.send()


def silent():
    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", extras={'k1':'v1'}, sound_disable=True)
    android_msg = jpush.android(alert="Hello, android msg")
    push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    push.platform = jpush.all_
    push.send()


def sms():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="a sms message from python jpush api")
    push.platform = jpush.all_
    push.smsmessage=jpush.smsmessage("a sms message from python jpush api",0)
    print (push.payload)
    push.send()

def validate():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.send_validate()



if __name__ == '__main__':
    audience(registration_id = ["13065ffa4e0d53730e1"])
