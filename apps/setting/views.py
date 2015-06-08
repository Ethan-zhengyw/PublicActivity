from django.shortcuts import render
from django.http import HttpResponse
import models as md

def setting(request):
    return render(request, 'setting.html', {'user': 'Ethan'})


def s_setting(request):
    print request.user.is_anonymous()

    oldPwd = request.POST['oldPwd']
    newPwd = request.POST['newPwd']
    confirmPwd = request.POST['confirmPwd']

    md.updatePwd('Amanda', oldPwd, newPwd, confirmPwd)

    return render(request, 'setting.html', {'user': 'Ethan'})


