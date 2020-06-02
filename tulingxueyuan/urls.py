from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher_app import views as v
from teacher import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #视图函数名称，只有名称，无括号和参数
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])',tv.withparam),
    # 比如约定，凡事由teacher模块处理的视图的url都以teacher开头
    #url(r'teacher/', include(teacher_url)),
    url(r'^teacher/',v.teacher),


    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),

    url(r'^youname/$', tv.extremParam,{'name':'刘大拿'}),

    url(r'^yourname/$',tv.revParse,name='askname'),

    url(r'^v2_exp/',v.v2_exception),

    url(r'^v10_1/',v.v10_1),
    url(r'^v10_2/',v.v10_2),
    url(r'^v11/',v.v11,name='v11'),

    url(r'^v8/',v.v8_get),
    url(r'^v9_get/',v.v9_get),
    url(r'^v9_post/',v.v9_post),
    url(r'^render_test/',v.render_test),
    url(r'^render2_test/',v.render2_test),
    url(r'^render3_test/',v.render3_test),
    url(r'^render1_to_res/',v.render4_test),
    url(r'^get404/',v.get404),
    url(r'^one/',v.one),
    url(r'^two/', v.two),
    url(r'^three/', v.three),
    url(r'^four/', v.four),
    url(r'^five_get/', v.five_get),
    url(r'^five_post/', v.five_post),

]
