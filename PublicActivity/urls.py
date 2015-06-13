# -*- coding: utf-8 -*-
import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    #     url   app-name.views.http-handler-name appname

    # test url
    #url(r'^index$', 'learn.views.index', name='index'),
    #url(r'^home$', 'learn.views.home', name='home'),
    #url(r'^add/$', 'calc.views.add', name='add'),
    #url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),
    #url(r'^homeTpl$', 'renderWithTpl.views.home', name='homeTpl'),

    url(r'^signup$', 'signup.views.signup', name='signup'),                 # 注册页面
    url(r'^service/signup$', 'signup.views.s_signup', name='s_signup'),     # 注册post表单地址

    url(r'^signin$', 'signin.views.signin', name='signin'),                 # 登录页面
    url(r'^service/signin$', 'signin.views.s_signin', name='s_signin'),     # 注册post表单地址

    url(r'^logout$', 'signin.views.logout', name='logout'),
    
    url(r'^create$', 'create.views.create', name='create'),                 # 发布公益活动的页面
    url(r'^service/create$', 'create.views.s_create', name='s_create'),     # Post的目的地址，后台创建新公益活动记录

    url(r'^setting$', 'setting.views.setting', name='setting'),                 # 设置页面
    url(r'^service/setting$', 'setting.views.s_setting', name='s_setting'),     # post表单地址

    url(r'^home$', 'home.views.explore', name='explore'),                   # 发现, 首页第一个Tab，查看所有公益活动
    url(r'^host$', 'home.views.host', name='host'),                         # 查看我关注的活动&我报名参加的公益活动

    url(r'^detail/(?P<aid>\w+)/$', 'create.views.create', name='create'),   # 发布公益活动的页面

    url(r'^admin/', include(admin.site.urls)),

    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.CSS_DIR}),
)
