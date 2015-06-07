from django.shortcuts import render
from django.http import HttpResponse
from model.user import *

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    user = User(username='Amanda', password='123456', user_type=1, email='123456@qq.com')
    user.save()
    for i in user:
        print i, user[i]
    return render(request, 'calc_home.html', {'string': 'par1'})
