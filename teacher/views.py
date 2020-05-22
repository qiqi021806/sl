from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.urlresolvers import reverse

'''
视图函数需要一个参数，类型因该是HttpRequest
'''
def do_normalmap(request):
    print('in do_normalmap')
    return HttpResponse('This is normalmap')

def withparam(request,year,month):
    return HttpResponse('This is with param {0}, {1}'.format(year,month))


def do_app(r):
    return HttpResponse('这是个子路由')


def do_param2(r,pn):
    return HttpResponse('page number is {0}'.format(pn))


def extremParam(r,name):
    return HttpResponse('My name is {0}'.format(name))

def revParse(r):
    return HttpResponse('Your requested url is {0}'.format(reverse('askname')))