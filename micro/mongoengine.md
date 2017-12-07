
#根据条件删除
    CourseCall.objects(taskerid=ObjectId(coursecall_id),ts=float(ts)).delete()
#更新一个list
    CourseTask.objects(courseid=courseid,classesid=classesid).update_one(push__task=task)
#删掉一个list中的东西
    Course.objects(courseid=courseid,classesid=classesid).update_one(pull__course=course)ca
#查询一个
    course = Course.objects(id=ObjectId(self.uid)).first()
#分页
    data = User.objects(id=ObjectId(collegec_lass))[0:5]
#更新一个
    Course.objects(courseid=courseid,classesid=classesid).update_one(pull__course=course)
    # Course.objects(id=ObjectId(_id)).modify(**kwargs)#两个都可以
