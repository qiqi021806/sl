from django.shortcuts import render
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