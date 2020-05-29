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
    
# 4、HttpResponseRedirect
- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
- 案例 ShowViews/views.py
        '''python
        url(r'^v10_1/',views.v10_1),
        url(r'^v10_2/',views.v10_2),
        url(r'^v11/',views.v11,name='v11'),        
        '''    
        def v10_1(request):
            return HttpResponseRedirect('/v11')
        def v10_2(request):
            return HttpResponseRedirect('/v11')
        def v11(request):
            return HttpResponse('哈哈，这是v11的访问返回')         
            
# 5、Request对象
- Request介绍
    - 服务器接收到HTTP协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面的完整路径，不包含域名
    - method:一个字符串，表示请求使用的HTTP方法，常用值包括：'get','post'
    - encoding:一个字符串，表示提交的数据的编码方式
        - 如果为None，则表示使用浏览器的默认设置，一般为UTF-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用
    - GET: 一个类似于字典的对象，包括get请求方式的所有参数
    - post: 一个类似字典的对象，包含POST请求方式的所有参数
    - files：一个类似于字典的对象，包含所有上传文件
    - cookies: 一个标准的python字典，包含所有的COOKIES，键和值
    - seeeion:一个既可读又可写的类似于字典的对象，表示当前的会话。
        - 只有当Django启用会话的支持是才用
        - 详细内容见“状态保持”
- 方法：
    - is_ajax():如果请求是通过xmlhttprequest发起的，则返回True.
-QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET，POST都是QueryDict类型的对象
    - 与Python字段不同，QueryDict类型的对象用来处理同一键带有多个值得情况
    - 方法get():根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist():根据键获取值
        -将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 与URL请求地址中的参数对应，位于？后面
    - 参数的格式是键值对，如：key1=value1
    - 多个参数之间，使用&连接，如： key1=value1&key2=value2 
    - 案例/views/v8_get
- POST属性
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中空间必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的。
    - 案例ShowViews/view/v9_post
        - settings中设置模板位置（已经设置完毕）
        - 设置get页面的urls和函数
            #'''python
                east/urls.py
                需要在路由文件中添加两个路由
                url(r'v9_get/',v.v9_get),
                url(r'v9_post/',v.v9_post),
            '''                        
            #'''python
                def v9_get(request):
                    return render_to_response('for_post.html').format
                def v9_post(request):
                    rst = ''
                    for k,v in request.POST.items():
                        rst += k + '-->' + v
                        rst += ','
                    return HttpResponse('Get value of Request is {0}'.format(rst))
            '''
- 手动编写视图            
    - 实验目的
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    - 分析：
        - django把所有的请求信息封装入request
        - django通过urls模块把相应请求跟事件处理函数链起来，并把request作为参数传入
        - 在相应的处理函数中，我们需要完成两个部分
            - 处理业务
            - 把结果封装并返回，我们可以使用简单HttpResponse,同样也可以自己处理此功能
        - 本案例不介绍业务处理，把目光集中在如何渲染结果并返回   
    - render(request,template_name[,context][,context_instance][,content_type])
        - 使用模板和一个给定的上下文环境，返回一个渲染的HttpResponse对象
        - request:django的传入请求
        - template_name:模板名称
        - content_instance:上下文环境
        - 案例参考代码 teacher_app/views/render_test
    - render_to_response    
        - 根据给定的上下文字典渲染给定模板，返回渲染后的HttpResponse 
- 系统内建视图
    - 系统内建视图，可以直接使用
    - 404 
        - defaults.page_not_found(request,template_name='404.html')
        - 系统引发Http404时触发
        - 默认窗体request_path变量给模板，即导致错误的URL
        - DEBUG=TRUE 则不会调用404，取而代之是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量
    - 500（server error）
        - defaults.server_error(request,template_name='500.html')
        - 需要DEBUG=False,否则不调用
    - 403（HTTP，Forbidden）视图
        - defaults.permission_denied(request,template_name='403.html')
        - 通过触发PermissionDenied触发
    - 400（bad request)视图
        - defaults.bad_request(request,template_name='400.html')
        - DEBUG=False
# 8、基于类的视图
- 和基于函数的视图的优势和区别：
    - HTTP方法的method可以有各自的方法，不需要使用条件分支解决
    - 可以使用OOP及时（例如：Mixin）
- 概述
    - 核心是允许使用不同的实例方法来响应不同的HTTP请求方法，而避开条件分支实现
    - as_view函数作为类的可调用入库，该方法创建一个实例并调用dispatch方法，按照请求方法
    方法没有定义，则引发HttpResponseNotAllowed
- 类属性使用
    - 在类定义时直接覆盖
    - 在调用as_vies的时候直接作为参数使用，例如：

# models 模型
- ORM 
    - ObjectRelationMap:把面向对象思想转换成关系数据库
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在gjango中，models负责跟数据库交互
- django链接数据库
    - 自带默认数据库Sqllite3
        - 关系型数据库
        - 轻量级
    - 建议开发用sqllite3,部署用mysql之类数据库
         - 切换数据库在settings中设置
         #django连接mysql
            '''
            DATABASES = [
                'default' = {
                    'ENGINE':'django.db.backends.mysql',
                    'NAME':'数据库名',
                    'PASSWORD':'数据库密码'
                    'HOST':'127.0.0.1'
                    'PORT':'3306'
                }
            ]    
            '''
        - 需要在项目文件下的__init__文件中导入pymysql包
        # 导入数据包
            '''
           import pymysql
           pymysql.install_as_MySQldb() 
            '''
# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.model的子类
    - class中所有的属性对应表格中的字段
    - 字段的类型都必须使用models.xxx 不能使用python中的类型
- 字段常用的参数
    - 1、max_length:规定数值的最大长度
    - 2、blank : 是否允许字段为空，默认不允许
    - 3、null:在DB中控制是否保存为NULL，默认为false
    - 4、default：默认值
    - 5、unique : 唯一
    - 6、verbose_name: 假名
- 数据库的迁移
    - 1、在命令行中，生成数据库迁移的语句（生成sql语句）
    #迁移
         '''
        python3 manage.py makemigrations    
         '''
    - 2、在命令行中，输入数据迁移的指令
    #迁移
        '''
        python3 manage.py migrate
        '''
        ps： 如果迁移中出现没有变化或者报错，可以尝试强制迁移
    #强制迁移命令
        '''
        python3 manage.py makemigrations 应用名
        python3 manage.py migrate 应用名
        '''
    - 3、对于默认数据库，为了避免出现混乱，如果数据库中没有数据，可以删掉自带的sqlite3数据库删除
    
- 4、查看数据库中的数据
    - 1、 启用命令行：python3 manage.py shell
        - ps：注意点，对ORM的操作分为静态函数和非静态函数两种，静态是指在内存中只有一份，
    - 2、 在命令行中带入对应的映射类
        - from 应用.models import 类名
    - 3、 使用objects属性操作数据库，objects是模型中实际和数据库进行交互的
            
    - 4、 查询命令
        - 类名.objects.all()查询数据库表中的所有内容，返回的结果是一个Query
        - 类名.objects.filter(条件)
    - 5、 保存数据
        - save()
        - 常用查找方法
        - 1、通用查找格式：属性名__（用下面的内容） = 值
            - gt：大于
            - gte:大于等于
            - lt: 小于
            - lte: 小于等于
            - range:范围
            - year: 年份
            - isnull: 是否为空   
        - 2、查找等于指定值得格式：属性名=值
        - 3、模糊查找： 属性名__（使用下面的内容） = 值
            - exact : 精确等于
            - iexact : 不区分大小写
            - contains : 包含
            - startwith : 以..开头
            - endwith : 以...结尾    
            

# 数据库关系
- 多表联查，利用多个表联合查找某一项或者多项信息。
    - 1：1  oneToOne
        - 建立关系，在模型任意一边即可，使用OneToOneField
        - add:
    # 添加数据
            - 添加没有关系的一边，直接实例化保存就可以
     
                >>> s = School()
                >>> s.school_id = 2
                >>> s.school_name = '河南工业大学'
                >>> s.save()
    # 实例化           
           - 添加有关系的一边，使用create方法或者使用实例化、
                # 方法1
                >>> m = Manager()
                >>> m.manager_id = 10
                >>> m.manager_name = '大拿'
                >>> m.my_school = s
                >>> m.save()
                # 方法2
                >>> m = Manager.objects.create(manager_id=20,manager_name='二钠',my_school=ss[0])
        - Query:
            - 有子表查母表，由子表的属性直接提取信息。
            >>> Manager.objects.get(manager_name='二钠').my_school.school_name
            - 由母表查子表，使用双下滑线
            >>> s = School.objects.get(manager__manager_name='大拿')
        - change:
            - 单个修改使用save
            - 批量修改使用update
            - 无论对子表还是对母表的修改
        - delete:
            - 直接使用delete进行删除。
            
    - 1:N OneToMany
        - 一个表格的一个数据项/对象等，可以有很多个另一个表格的数据项。
        - 比如：一个学校可以有很多个老师，但一个老师只能在一个学校里上班。
        - 使用上：
            - 使用ForeignKey
            - 在多的那一边，比如上边的例子就是在Teacher的表格里进行定义
        - Add:
            - 跟一对一方法类似，通过create和new来添加    
            - create: 把属性都填满，然后不需要手动保存
            - new:可以属性或者参数为空，必须用save保存。
        - Query: 
            - 以学校和老师例子为准。
            - 如果知道老师，查学校，则通过增加的关系属性，直接使用
            - 例如：查找t1老师，是哪个学校的。  
            - 反查：
                - 有学校，我想查下这个学校所有老师，则需要在老师模型名称的小写下直接加下划线set,
                    用来表示 
                    >>> ss[1].teacher_set.all()
       
    - N:N ManyToMany
        - 表示任意一个表的数据可以拥有对方表格多项数据，反之亦然，
        - 比如典型例子就是老师和学生关系。
        - 使用上，在任意一方，使用MangToMany 定义，只需要定义一边
        - Add：
            - 添加老师，则在student.teachers.add()
        - Query:
            - 查询。