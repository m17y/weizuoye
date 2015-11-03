#Ubuntu
###Mysql
http://www.jb51.net/os/Ubuntu/38725.html

    net start mysql //启动mysql服务
    2、net stop mysql //停止mysql服务　
    3、mysql -h主机地址 -u用户名 －p用户密码 //进入mysql数据库
    4、quit //退出mysql操作
    5、mysqladmin -u用户名 -p旧密码 password 新密码 //更改密码
    6、grant select on 数据库.* to 用户名@登录主机 identified by "密码" //增加新用户 
    
no module named MySqldb

    The correct command is:
    sudo ap-get install python-mysqldb
    
錯誤提示：Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your database and pytz installed?
    解決方法：USE_TZ = False