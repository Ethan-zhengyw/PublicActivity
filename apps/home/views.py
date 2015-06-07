# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def explore(request):
    return HttpResponse('发现 首页 第一个Tab 查看所有公益活动')


def host(request):
    return HttpResponse('发现 首页 第二个Tab 查看所有我关注的公益活动and报名的')
