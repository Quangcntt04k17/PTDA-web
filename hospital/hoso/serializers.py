# hoso/serializers.py

from rest_framework import serializers
from .models import BenhNhan, HoSoBenhAn

class BenhNhanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenhNhan
        fields = '__all__'



class HoSoBenhAnSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoSoBenhAn
        fields = '__all__'  # Bao gồm tất cả các trường của model

    def validate_benhNhan(self, value):
        # Kiểm tra xem bệnh nhân có tồn tại trong cơ sở dữ liệu hay không
        if not BenhNhan.objects.filter(maBenhNhan=value.maBenhNhan).exists():
            raise serializers.ValidationError("Bệnh nhân không tồn tại.")
        return value
