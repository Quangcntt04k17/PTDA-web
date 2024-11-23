from django.urls import path
from hoso import views
from.views import DanhSachHosoView,DanhSachBenhAnView,ThemHosoView,ThemBenhAnView,TimKiemCCCDView,LocBenhAnView

urlpatterns = [
    path('hosolist/',DanhSachHosoView.as_view()  , name='danh_sach_hoso'),
    path('benhanlist/', DanhSachBenhAnView.as_view(), name='benhanlist'),
    path('addhoso/', ThemHosoView.as_view(), name='them_hoso'),
    path('addbenhan/',ThemBenhAnView.as_view(), name='them_benh_an'), 
    path('timkiem/', TimKiemCCCDView.as_view(), name='tim_kiem_cccd'),
    path('loc/', LocBenhAnView.as_view(), name='loc_benh_an'),
]