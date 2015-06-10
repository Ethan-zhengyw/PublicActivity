from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def setting(request):
    #TODO check whether user have signin
    return render(request, 'setting.html', {'user': 'Ethan'})


def s_setting(request):

    oldPwd = request.POST['oldPwd']
    newPwd = request.POST['newPwd']
    confirmPwd = request.POST['confirmPwd']

    md.updatePwd('Amanda', oldPwd, newPwd, confirmPwd)

    introduction = request.POST['introduction']
    gender = request.POST['gender']
    md.updateBasicInfo(introduction, gender)

    return HttpResponseRedirect('/setting')
