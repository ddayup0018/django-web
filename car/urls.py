from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('car', views.car,name='car'),
    path('car/new', views.new,name='new'),
    path('car/new_insert', views.new_insert,name='new_insert'),
    path('car/anpai/<str:ucym>', views.anpai,name='anpai'),
    path('car/anpai_insert', views.anpai_insert,name='anpai_insert'),
    path('car/guihuan/<str:ucym>', views.guihuan,name='guihuan'),
    path('car/guihuan_update', views.guihuan_update,name='guihuan_update'),
    path('car/del_one/<str:ucym>', views.del_one,name='del_one'),
    path('car/del_all', views.del_all,name='del_all'),
    path('car/del_allinfo', views.del_allinfo,name='del_allinfo'),
    path('car/edit/<str:ucym>', views.edit,name='edit'),
    path('car/edit_update', views.edit_update,name='edit_update'),
    path('car/search', views.search,name='search'),
    # path('car/search/find_cym', views.find_cym,name='find_cym'),
    # path('car/search/find_jsy', views.find_jsy,name='find_jsy'),
    # path('car/search/find_date', views.find_date,name='find_date'),
    path('car/search/find_other', views.find_other,name='find_other'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
