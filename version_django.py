# -*- coding:utf-8 -*- 

import django 

def show_version():
	print('django_version:%s'%django.get_version())

if __name__ == '__main__':
	show_version()