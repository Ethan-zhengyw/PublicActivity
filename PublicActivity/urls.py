# -*- coding: utf-8 -*-

import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^signup$', 'signup.views.signup', name='signup'),                                 # 注册页面
    url(r'^checkEmail$', 'signup.views.checkUsedEmail', name='checkEmail'),
    url(r'^service/signup$', 'signup.views.s_signup', name='s_signup'),                     # 注册post表单地址

    url(r'^signin$', 'signin.views.signin', name='signin'),                                 # 登录页面
    url(r'^service/signin$', 'signin.views.s_signin', name='s_signin'),                     # 注册post表单地址

    url(r'^logout$', 'signin.views.logout', name='logout'),
    
    url(r'^create$', 'create.views.create', name='create'),                                 # 发布公益活动的页面
    url(r'^service/create$', 'create.views.s_create', name='s_create'),                     # Post的目的地址，后台创建新公益活动记录

    url(r'^edit/(\w+)$', 'edit.views.edit', name='edit'),                                 
    url(r'^service/edit/(\w+)$', 'edit.views.s_edit', name='s_edit'),                    


    url(r'^setting$', 'setting.views.setting', name='setting'),                             # 设置页面
    url(r'^service/setting$', 'setting.views.s_setting', name='s_setting'),                 # post表单地址

    url(r'^$', 'home.views.explore', name='explore'),
    url(r'^home$', 'home.views.explore', name='explore'),                                   # 发现, 首页第一个Tab，查看所有公益活动
    url(r'^host$', 'home.views.host', name='host'),                                         # 查看我关注的活动&我报名参加的公益活动

    url(r'^details/(\w+)$', 'details.views.details', name='details'),                       # 公益活动详情页面

    url(r'^service/details/setPar/(\w+)$', 'details.views.setPar', name='setPar'),          # 报名
    url(r'^service/details/unsetPar/(\w+)$', 'details.views.unsetPar', name='unsetPar'),    # 取消报名

    url(r'^service/details/setCon/(\w+)$', 'details.views.setCon', name='setCon'),          # 关注
    url(r'^service/details/unsetCon/(\w+)$', 'details.views.unsetCon', name='unsetCon'),    # 取消关注
    url(r'^service/details/makeComment/(\w+)$', 'details.views.makeComment', name='makeComment'),    # 评论

    url(r'^manager$', 'manager.views.manager', name='manager'),                             
    url(r'^service/setPass/(\w+)$', 'manager.views.setPass', name='setPass'),
    url(r'^service/setFailPass/(\w+)$', 'manager.views.setFailPass', name='setFailPass'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.CSS_DIR}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.JS_DIR}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.IMG_DIR}),

    url(r'^bootstrap/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.BOOTSTRAP_DIR}),
    url(r'^jquery/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.JQUERY_DIR}),
)
