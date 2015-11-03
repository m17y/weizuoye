#coding=utf-8 
from django.db import models
from django.core.urlresolvers import reverse
from collections import OrderedDict
# Create your models here.
class  Teacher(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	password = models.CharField(max_length=50)
	def __unicode__(self):
        		return self.name 

class  Student(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	password = models.CharField(max_length=50)
	def __unicode__(self):
        		return self.name 
class SubjectManager(models.Model):
    def get_Subject_list(self):
        subjects = Subject.objects.all()
        subjects_list = []
        for i  in range(len(subjects)):
           	subjects_list.append([])
        for i  in range(len(subjects)):
            temp = Subject.objects.get(name = subjects[i]) #获取当前标签
            posts = temp.article_set.all() #获取当前标签下的所有文章
            subjects_list[i].append(subjects[i].name)
            subjects_list[i].append(len(posts))
        return subjects_list
        
class Subject(models.Model):
    name = models.CharField(max_length=20,blank=True)
    creat_time = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=10,blank=True)

    objects = models.Manager()#默认的管理器
    subject_list = SubjectManager()#自定义的管理器


    @models.permalink
    def get_absolute_url(self):
        return('subjectDetail', (), {
      'subject':self.name})
    def __unicode__(self):
        return self.name

