from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user,name='user'),
    path('user/new', views.new,name='new'),
    path('user/new_insert', views.new_insert,name='new_insert'),
    path('user/del_one/<str:uxm>', views.del_one,name='del_one'),
    path('user/del_all', views.del_all,name='del_all'),
    path('user/find_one', views.find_one,name='find_one'),
    path('user/edit/<int:uid>', views.edit,name='edit'),
    path('user/edit_update', views.edit_update,name='edit_update'),
]
