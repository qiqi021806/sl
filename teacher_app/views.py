from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
from django.core.urlresolvers import reverse

def teacher(r):
   return  HttpResponse('这是一个teacher的一个视图')

def v2_exception(r):
    raise Http404
    return  HttpResponse('OK')


def v10_1(request):
    return HttpResponseRedirect('/v11')


def v10_2(request):
    return HttpResponseRedirect(reverse('v11'))


def v11(request):
    return HttpResponse('哈哈，这是v11的访问返回')


def v8_get(request):
    rst = ''
    for k,v in request.GET.items():
        rst += k + '-->' + v
        rst += ','
    return HttpResponse('Get value of Request is {0}'.format(rst))

def v9_get(request):
    return render_to_response('for_post.html')

def v9_post(request):
    rst = ''
    for k, v in request.POST.items():
        rst += k + '-->' + v
        rst += ','
    return HttpResponse('Get value of Request is {0}'.format(rst))

def render_test(request):
    # 环境变量
    #c = dict()
    rsp = render(request,"render.html")
    return rsp


def render2_test(request):
    # 环境变量
    c = dict()
    c['name']='Shao Liang '
    c['name2'] = 'Shao 1 Liang '
    c['name3'] = 'Shao 2 Liang '
    rsp = render(request,"render2.html",context=c)
    return rsp

def render3_test(request):
    from django.template import loader

    # 得到模板
    t = loader.get_template("render2.html")
    r = t.render({'name':'liudana','name2':'shaoliang'})
    return HttpResponse(r)

def render4_test(request):
    # 反馈回模板render2.html
    rsp = render_to_response('render2.html',context={'name':'shaoliang'})
    return rsp

def get404(r):
    from django.views import defaults
    return defaults.page_not_found(r,template_name='render.html')

def one(r):
    rsp = render(r, "one.html")
    return rsp

def two(r):
    #  用来存放想模板中传递的数据
    ct = dict()
    ct['name'] = '王晓静'
    rsp = render(r, "two.html",context=ct)
    return rsp

def three(r):
    #  用来存放想模板中传递的数据
    ct = dict()
    ct['score']=[99,87,23,100,83,96]
    rsp = render(r, "three.html",context=ct)
    return rsp

def four(r):
    #  用来存放想模板中传递的数据
    ct = dict()
    ct['name']='李晓静'
    rsp = render(r, "four.html",context=ct)
    return rsp

def five_get(r):

    rsp = render(r, "five_get.html")
    return rsp

def five_post(r):
    print(r.POST)
    rsp = render(r, "one.html")
    return rsp