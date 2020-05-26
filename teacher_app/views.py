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





