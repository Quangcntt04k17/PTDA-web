from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer

class PatientAPI(APIView):

    # Lấy chi tiết tài nguyên
    def get(self, request, pk=None):
        try:
            if pk:
            # Lấy thông tin chi tiết một bệnh nhân
                patient = Patient.objects.get(pk=pk)
                serializer = PatientSerializer(patient)
                return Response(serializer.data)
            else:
                # Lấy danh sách bệnh nhân
                patients = Patient.objects.all()
                serializer = PatientSerializer(patients, many=True)
                return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Tạo tài nguyên mới
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Cập nhật toàn bộ tài nguyên
    def put(self, request, pk):
        try: 
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Cập nhật một phần tài nguyên
    def patch(self, request, pk):
        try: 
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Xóa tài nguyên
    def delete(self, request, pk):
        try: 
            patient = Patient.objects.get(pk=pk)
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)


class MedicalRecordAPI(APIView):

    # Lấy chi tiết tài nguyên
    def get(self, request, pk=None):
        try:
            medicalRecord = MedicalRecord.objects.get(pk=pk)
            serializer = MedicalRecordSerializer(medicalRecord)
            return Response(serializer.data)
        except MedicalRecord.DoesNotExist:
            return Response({"error": "MedicalRecord not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Tạo tài nguyên mới
    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Cập nhật toàn bộ tài nguyên
    def put(self, request, pk):
        try: 
            medicalRecord = MedicalRecord.objects.get(pk=pk)
            serializer = MedicalRecordSerializer(medicalRecord, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicalRecord.DoesNotExist:
            return Response({"error": "MedicalRecord not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Cập nhật một phần tài nguyên
    def patch(self, request, pk):
        try: 
            medicalRecord = MedicalRecord.objects.get(pk=pk)
            serializer = MedicalRecordSerializer(medicalRecord, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicalRecord.DoesNotExist:
            return Response({"error": "MedicalRecord not found"}, status=status.HTTP_404_NOT_FOUND)
        
    # Xóa tài nguyên
    def delete(self, request, pk):
        try: 
            medicalRecord = MedicalRecord.objects.get(pk=pk)
            medicalRecord.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MedicalRecord.DoesNotExist:
            return Response({"error": "MedicalRecord not found"}, status=status.HTTP_404_NOT_FOUND)
