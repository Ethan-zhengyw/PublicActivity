# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('公益活动index')

def home(request):
    return HttpResponse('公益活动home')

def testfunc():
    print 'a'
