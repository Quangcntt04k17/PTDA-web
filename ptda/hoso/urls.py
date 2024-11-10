from django.urls import path
from . import views
from .views import tim_kiem_cccd_view
from .views import danh_sach_benh_an_view,loc_benh_an

urlpatterns = [
    path('hosolist', views.danh_sach_hoso, name='danh_sach_hoso'),
     path('benhanlist', danh_sach_benh_an_view, name='danh_sach_benh_an'),
    path('addhoso', views.them_hoso, name='them_hoso'),
    path('addbenhan', views.them_benh_an, name='them_benh_an'), 
    path('timkiem', tim_kiem_cccd_view, name='tim_kiem_cccd'),
    path('timkiem', tim_kiem_cccd_view, name='chi_tiet_hoso_view'),
    path('loc', loc_benh_an, name='loc_benh_an'),
]

