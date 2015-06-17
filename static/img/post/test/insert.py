# coding=utf-8
from user import *
import insert_acts as ia

users = [
    {
        'username': 'Tom',
        'password': md5HashPwd('Tom'),
        'email': 'Tom@Tom.com',
        'user_type': 2,
        'avatar': '/img/avatar/1.jpg'
    },

    {
        'username': 'Ann',
        'password': md5HashPwd('Ann'),
        'email': 'Ann@Ann.com',
        'user_type': 2,
        'avatar': '/img/avatar/2.jpg'
    },

    {
        'username': 'admin',
        'password': md5HashPwd('admin'),
        'email': 'admin@admin.com',
        'user_type': 0,
        'avatar': '/img/avatar/3.jpg'
    },

    {
        'username': '三余社',
        'password': md5HashPwd('sys'),
        'email': 'sys@sys.com',
        'user_type': 1,
        'avatar': '/img/avatar/3.jpg'
    },

    {
        'username': '羽协',
        'password': md5HashPwd('yx'),
        'email': 'yx@yx.com',
        'user_type': 1,
        'avatar': '/img/avatar/4.jpg'
    },

    {
        'username': '青协',
        'password': md5HashPwd('qx'),
        'email': 'qx@qx.com',
        'user_type': 1,
        'avatar': '/img/avatar/6.jpg'
    },
]

def insert_users():

    for user in users:
        u = User(
            username=user['username'],
            password=user['password'],
            email=user['email'],
            user_type=user['user_type'],
            avatar=user['avatar'],
        )

        if not User.objects(email=u.email).first():
            u.save()



insert_users()
ia.insert_acts()
