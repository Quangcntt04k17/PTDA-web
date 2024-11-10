from django.contrib import messages
from .models import Hoso, BenhAn
from django.shortcuts import render, redirect
from .forms import HosoForm, BenhAnForm
from datetime import datetime

def danh_sach_hoso(request):
    danh_sach_hs = Hoso.objects.all()
    return render(request, 'hoso/danh_sach_hoso.html', {'danh_sach_hs': danh_sach_hs})




def danh_sach_benh_an_view(request):
    danh_sach_ba = BenhAn.objects.all()
    sort_option = request.GET.get('sort', None)
    reset_filter = request.GET.get('reset', 'false')

    if reset_filter == 'true':
        return render(request, 'hoso/danh_sach_benh_an.html', {'danh_sach_ba': danh_sach_ba})
    if sort_option == 'latest':
        danh_sach_ba = danh_sach_ba.order_by('-ngay_kham')
    elif sort_option == 'oldest':
        danh_sach_ba = danh_sach_ba.order_by('ngay_kham')
    return render(request, 'hoso/danh_sach_benh_an.html', {'danh_sach_ba': danh_sach_ba})

def them_hoso(request):
    if request.method == 'POST':
        form = HosoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Lưu hồ sơ thành công !")
    else:
        form = HosoForm()
    return render(request, 'hoso/them_hoso.html', {'form': form})



def them_benh_an(request):
    if request.method == 'POST':
        form = BenhAnForm(request.POST)
        if form.is_valid():
            benh_an = form.save(commit=False)
            benh_an.so_cccd = form.cleaned_data['so_cccd']
            benh_an.save()
            messages.success(request, "Lưu hồ sơ thành công !")
    else:
        form = BenhAnForm()

    return render(request, 'hoso/them_benh_an.html', {'form': form})






def tim_kiem_cccd_view(request):
    search = request.GET.get('so_cccd', None)
    hoso = None
    benh_an_list = []

    if search:
        # Lấy thông tin bệnh nhân từ  Hoso
        hoso = Hoso.objects.filter(so_cccd=search).first() 
        if hoso:
            # Lấy danh sách bệnh án dựa trên số CCCD
            benh_an_list = BenhAn.objects.filter(so_cccd=search).order_by('-ngay_kham') 

    return render(request, 'hoso/timkiem_cccd.html', {'hoso': hoso, 'benh_an_list': benh_an_list, 'search': search})




from .forms import FilterBenhAnForm


def loc_benh_an(request):
    form = FilterBenhAnForm()
    danh_sach_benh_an = []

    if request.method == 'POST':
        form = FilterBenhAnForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Lọc hồ sơ bệnh án theo khoảng thời gian
            danh_sach_benh_an = BenhAn.objects.filter(ngay_kham__range=(start_date, end_date)).order_by('-ngay_kham')

    return render(request, 'hoso/loc_benh_an.html', {'form': form, 'danh_sach_benh_an': danh_sach_benh_an})
