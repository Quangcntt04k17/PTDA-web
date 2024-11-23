from django.urls import path
from .views import PatientAPI, MedicalRecordAPI

urlpatterns = [
    # API cho bệnh nhân
    path('patients/', PatientAPI.as_view(), name='patient-list-create'),  # GET danh sách, POST tạo mới
    path('patients/<int:pk>/', PatientAPI.as_view(), name='patient-detail'),  # GET, PUT, PATCH, DELETE theo ID

    # API cho bệnh án
    path('medical-records/', MedicalRecordAPI.as_view(), name='medicalrecord-create'),  # POST tạo mới
    path('medical-records/<int:pk>/', MedicalRecordAPI.as_view(), name='medicalrecord-detail'),  # GET, PUT, PATCH, DELETE theo ID
]
