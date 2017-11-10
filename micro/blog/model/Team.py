# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
import datetime,time
from mongoengine import *
from Base import connect,BaseObject
from Assignment import User
# connect('mydb')


class Team(Document,BaseObject):
    """社团类"""
    teamcount = property(lambda self: self.usercount())
    name = StringField(max_length=30)
    email = EmailField(required=False)
    description = StringField()
    school = StringField(max_length=30)
    owner =  ReferenceField(User, reverse_delete_rule=CASCADE)
    leaguer = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    created_time = FloatField()
    @property
    def teamrcount(self):
        team_count = Team.objects(name=self.name).count()
        return user_count



class TeamActivity(Document,BaseObject):
    """社团类"""
    name = StringField(max_length=30)
    description = StringField()
    owner =  ReferenceField(User, reverse_delete_rule=CASCADE)
    leaguer = ListField(ReferenceField(User,reverse_delete_rule=PULL))
    created_time = FloatField()
    end_time = FloatField()
    team = ReferenceField(Team, reverse_delete_rule=CASCADE)