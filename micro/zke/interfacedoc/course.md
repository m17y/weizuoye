# 课程

#获得用户课程信息
method:get
paths:/course
consumes:application/json
request:{
    ownerid:'xxx'(必填),
}
return：{
    courses:{},
}
#添加用户课程
method:post
paths:/course
consumes:application/json
request:{
    code:'xxx'(课程code)(必填),
}
return：{
    status:True(False),
    msg:''
}

#删除用户课程
method:delete
paths:/course
consumes:application/json
request:{
    courseid:'xxx'(课程id)(必填),
}
return：{
    status:True(False),
    msg:''
}

#更新用户课程
method:put
paths:/course
consumes:application/json
request:{
    name:'xxx',
}
return：{
    status:True(False),
    msg:''
}