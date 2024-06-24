from django.urls import re_path
from . import views

app_name = 'myshop'

urlpatterns = [
    re_path(r'^home_page$', views.home_page, name='home_page'),
    re_path(r'^$', views.home_page, name='home_page'),
    re_path(r'^(?P<product_id>\d+)/(?P<product_slug>\w+)/$', views.product_detail, name='product_detail'),
    re_path(r'^product_list/$', views.product_list, name='product_list'),
    re_path(r'^categories/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
]