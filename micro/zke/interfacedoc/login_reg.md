# 用户注册登陆

#用户登陆
method:post
paths:/login
consumes:application/json
request:{
    name:'name'(必填)
    password:'password'(必填)
}
return：{
    status:True(False),
    msg:''
}

#用户注册
method:post
paths:/reg
consumes:application/json
request:{
    nickname:'suyf',
    name:'苏亚飞',
    email:'1007@qq.com',
    password:'xxxx',
}
return：{
    status:True(False),
    msg:''
}
