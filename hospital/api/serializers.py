from rest_framework import serializers
from .models import Patient, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'




'''

Trong Django REST Framework (DRF),
 serializers đóng vai trò rất quan trọng trong việc chuyển đổi dữ liệu giữa các loại dữ liệu phức tạp (như các mô hình Django)
 và các định dạng dễ sử dụng hơn, chẳng hạn như JSON hoặc XML. 
'''