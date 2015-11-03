#参考网址

http://segmentfault.com/q/1010000002523354/a-1020000002526934

    sudo apt-get install python-dev
    sudo apt-get install python-pip
    sudo pip install pip --upgrade
    sudo apt-get install libpcre3 libpcre3-dev
    sudo apt-get install zlib1g-dev
    sudo apt-get install nginx-full
    
#本機部署apache+wsgi+django 

	參考部署地址：http://www.cnblogs.com/CSGrandeur/p/3741871.html

1解決 css樣式不出來的問題

	apache的httpd.conf里，使用
	Alias /static /home/a21/static
	
	引自：http://www.dataguru.cn/thread-68997-1-1.html
	
2.apache2 log輸出錯誤提示

	AppRegistryNotReady: The translation infrastructure cannot be initialized before the apps registry is ready
	解決方法：版本的问题  
		根据官方文档，django.wsgi 确实是这么写的
	
		application = django.core.handlers.wsgi.WSGIHandler()

		但是实际上，可能是版本的问题，我用的是django 1.6 的，换成:

		from django.core.wsgi import get_wsgi_application
		application = get_wsgi_application()
	引自：http://bbs.csdn.net/topics/390878013?page=1#post-400503865