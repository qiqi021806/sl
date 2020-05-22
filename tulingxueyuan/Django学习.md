# Django 
    - 环境： 
        Python 3.6 
        django 1.8 
        [中文教程]https://yiyibooks.cn/
        django 架站的16堂课
        
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list: 显示当前环境安装的包
    - conda env list:显示安装的虚拟环境列表。
    - conda create -n env_name python=3.6
    - 激活（conda）的虚拟环境
        - （linux）source activate env_name
        -  (win)activate env_name
    - pip inatall django=1.8
     
# 后台需要的流程

# 创建第一个Django程序
   - 命令行启动
        - django-admin startproject tulingxueyuan
        - cd tulingxueyuan
        - python manage.py runserver
   - pycharm 启动
        - 需要配置
 
 # 1、路由系统-urls
 - 创建APP
    - APP:负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
 - 路由
    - 按照具体的请求URL,导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了re
    - url的具体格式如urls.py中所示。 
- 需要关注的两点：
    - 1、接受的URL是什么，即如何用RE对传入的URL进行匹配。
    - 2、 已知的URL匹配到哪个处理模块。
- URL 匹配规则
    - 从上到下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对，主要对应URL包含子URL的情况
    - 子url一旦被调用，则不会返回到主URL
        -'/one/two/three/'
    - 正则以r开头，表示不需要转义，注意尖号(^)和美元符号($)
        - '/one/two/three' 配对r'^one/'
        - 'oo/one/two/three' 不配对r'^one/'
        - '/one/two/three' 配对r'three/$'
        - '/one/two/three/oo/' 不配对r'three/$'
        - 开头不需要有反斜杠
    - 如果从上向下都没找到合适的匹配内容，则报错
# 2 、正常映射
- 把某一个符合RE的url映射到实物处理行数中去
    - 举例如下：
        '''
        from teacher import views as tv
        urlpatterns = [
            # Examples:
            # url(r'^$', 'tulingxueyuan.views.home', name='home'),
            # url(r'^blog/', include('blog.urls')),
        
            url(r'^admin/', include(admin.site.urls)),
            #视图函数名称，只有名称，无括号和参数
            url(r'^normalmap/', tv.do_normalmap),
            url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])',tv.withparam)
        
        ]
        '''
# 3、url中带参数映射
- 在事件处理代码中需要由URL传入参数，形如/myurl/param中的param
- 参数都是字符串形式，如果需要整数形式，需要自行转换
- 通常的形式如下：
        '''
        /search/page/432 中的432需要经常性变换，所以设置为参数比较合适。
        '''
# 4、URL在app中处理
- 如果所有应用url都集中在tulingxueyuan/urls.py中，可能导致文件的臃肿
- 可以把url具体功能逐渐分散到每个app中
    - 从django.conf.urls中导入include
    - 注意此时re部分的写法
    - 添加include导入
- 使用方法
    - 确保
    - 同样可以使用参数
# 5、url中的嵌套参数
- 捕获某个参数的一部分
    - 例如url /index/page-3,需要捕获数字3作为参数
        '''
        url(r'index_1/(page-(\d+)/)?$',tv.myindex_1),# 不太好
        url(r'index_2/(?:page-(?P<page_number>\d+)/)?$',tv.myindex_2),# 好
        
        '''
    - 以上例子会得到两个参数，但?:表明忽略此参数
# 6、传递额外参数
- 参数不仅仅来自URL，还可能是我们自己定义的内容
    '''
    url(r'extrem/$',sv.extremParam,{'name':'liuying'}),
        
    '''
- 附件参数同样适用于include语句，此时对include内所有都添加
# 7、url的反向解析
- 防止硬编码
- 本质上是对每一个url进行命名
- 以后再编码代码中使用url的值，原则上都应该使用反向解析

# views 视图
# 1、视图概述
- 视图即视图函数，接收web请求并返回web响应的事务处理函数
- 响应值符合http协议要求的任何内容，包括json,string,html等
- 本章忽略事务处理，重点在如何返回处理结果上
# 2 其他简单视图
- django.http 给我们提供很多和HttpRespense类似的简单视图
通过查看Django.http 代码可以知道
- 此类视图使用方法基本类似，可以通过return语句直接反馈返回给浏览器
- Http404为Exception子类，所以需要raise使用
# 3、HttpResponse详解
- 方法
    -init : 使用页内容实例化HttpResponse对象
    - write(content),以文件的方式写
    - flush()：以文件方式输出缓存区
    - set_cookie(key，value='',max_age=None，expires=None):设置Cookie
        - key ,value 都是字符串类型
        - max_age是一个整数，表示在指定秒后过期
        - expries是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，
        - max_age与expires二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key):删除指定的key的Cookie,如果key不存在则什么也不发生
    