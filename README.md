#链接
    权限控制：
        http://ocaml.org/learn/tutorials/structure_of_ocaml_programs.zh.html
    Python 教程
        http://www.kuqin.com/abyteofpython_cn/
    Python中文社区
        http://www.pythontab.com/
    Django教程
        http://www.ziqiangxuetang.com/django/django-tutorial.html
    DjangoBook
        http://docs.30c.org/djangobook2/
    Django官网
        http://www.djangoproject.com/
    Django中文论坛
        http://www.djangochina.cn/
    
    [示例项目地址]
        https://coding.net/u/sis/p/WorkTime/git/tree/example-blog/
        http://krsu.coding.io/
    [Web Design]
        Web原型
        http://www.webppd.com/
    [现代简明魔法-python]
        Django入门教程
        http://www.nowamagic.net/academy/part/13/286
        

#步骤

###1: 建立项目

	新建Project ：django-admin.py startproject project-name

	新建App ： django-admin.py startapp app-name

	同步数据库 ：python manage.py makemigrations
				 python manage.py migrate
	python manage.py syncdb
		 	
	引入依赖：
	            pip install -r requirements/dev.txt
	　ubuntu上安装mysql非常简单只需要几条命令就可以完成。
　　1. sudo apt-get install mysql-server
 
　　2. apt-get isntall mysql-client
 
　　3.  sudo apt-get install libmysqlclient-de

###2: 汉化

	Django设置后台中文面板，修改settings.py文件，只需要修改两行：

	LANGUAGE_CODE = ‘zh-CN’

	TIME_ZONE = ‘Asia/Shanghai’

###3:后台美化

Installation

	pip install django-admin-bootstrapped (virtualenv highly suggested)

	add django_admin_bootstrapped into the INSTALLED_APPS list beforedjango.contrib.admin

	have fun!

Your INSTALLED_APPS should look like this:

	INSTALLED_APPS = (
		'django_admin_bootstrapped',
		'django.contrib.admin',

		...
	)
	
	
###环境搭建
	Linux ubuntu: 14
	Python: 2.7
	Django: 1.8
	Mysql: 5.6.24
	编辑器：Vim
	
###开发模式
	快速原型模型 敏捷开发
	[http://blog.sina.com.cn/s/blog_5d2070030101b9m0.html]
	
###需求背景:

###硬件背景:

###知识背景:

###整个开发用到的软件如下:

###实现的功能如下:

###更新历史:

###Call Me：

    email：100714131@qq.com