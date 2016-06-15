from django.conf.urls import url
from .views import *

urlpatterns  = [
	url(r'^$',main,name='main'),
	url(r'^medicamentos/',medicamentos,name='medicamentos'),
	url(r'^formula/',formula,name='formula'),
]
