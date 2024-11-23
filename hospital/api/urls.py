from django.urls import path
from .views import BenhNhanAPI, GetBacSiAPI,HoSoBenhAnAPI
from api import views 

from .views import *


urlpatterns = [

    path('viewsAPIBacSi/',GetBacSiAPI.as_view(),name="bac-si-list"),
    path('viewsAPIBenhNhan/',BenhNhanAPI.as_view(),name="benh-nhan-list"),
    path('viewsAPIHoSo/',HoSoBenhAnAPI.as_view(),name="ho-so-list"),
    
    path('viewsAPIBacSi/<int:maBacSi>', GetBacSiAPI.as_view(), name='bac-si-detail'),  # PUT, DELETE
    path('viewsAPIBenhNhan/<int:maBenhNhan>', BenhNhanAPI.as_view(), name='benh-nhan-detail'),  # PUT, DELETE
    path('viewsAPIHoSo/?maBenhAn=<int:maBenhAn>', HoSoBenhAnAPI.as_view(), name='ho-so-detail'),  # PUT, DELETE

    # thu tu thoi gian
    path('danh_sach_hoso_view/', views.danh_sach_hoso_view, name='ho_so_benh_an_theo_thoi_gian'),

    # theo ngay
    path('ho_so_benh_an_date/', views.ho_so_benh_an_theo_ngay, name='ho_so_benh_an_theo_ngay'),

    # theo khoang ngay
    path('ho_so_khoang_ngay/', views.ho_so_benh_an_theo_khoang_ngay, name='ho_so_benh_an_theo_khoang_ngay'),

    # quang
    path('hosolist/',DanhSachHosoView.as_view()  , name='danh_sach_hoso'),
    path('benhanlist/', DanhSachBenhAnView.as_view(), name='benhanlist'),
    path('addhoso/', ThemHosoView.as_view(), name='them_hoso'),
    path('addbenhan/',ThemBenhAnView.as_view(), name='them_benh_an'), 
    path('timkiem/', TimKiemCCCDView.as_view(), name='tim_kiem_cccd'),
]
