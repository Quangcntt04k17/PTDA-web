# hoso/serializers.py

from rest_framework import serializers
from .models import Hoso, BenhAn

class HosoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoso
        fields = '__all__'



class BenhAnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenhAn
        fields = ['ma_benh_an', 'ngay_kham', 'khoa_dieu_tri', 'chuan_doan','dieu_tri']
