mongod --dbpath /root/mongo/db
redis-server
celery -A task_server worker --loglevel=info
redis-cli

kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())

#supervisor
#重新启动进程之前必须运行此命令
unlink /tmp/supervisor.sock
#启动supervisor进程
supervisord -c /etc/supervisor/supervisord.conf 
supervisorctl -> start weizuoye 启动程序
＃　参考网址
#TODO 莘莘学子（名字？是否改名）
# TODO 课程帮，同学或者老师之间课程有偿帮助
# TODO 积分制度，粘合用户

1.学生签到
２．课程作业自动评阅
３．社团系统
４．课程帮(同学或者老师之间课程有偿帮助)
5.圈子。分享发布好玩的东西，用户之互相赞，粘合用户（有可能是最新的新闻学校或者学或其他，好玩的课程分享））
６．求贤（社招模块）（这个我想是以后重点）
７．校园公告
８．积分制度，（仿照知乎，用来人才归纳以及为以后社招做推荐）
９．社会兼职模块
10.余塘
11.陪陪（陪看电影陪吃陪喝陪睡）
