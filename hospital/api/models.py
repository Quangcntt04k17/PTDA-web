from django.db import models

class Patient(models.Model):
    # Thông tin cơ bản của bệnh nhân
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Nam'), ('Female', 'Nữ')])
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.id}"

class MedicalRecord(models.Model):
    # Thông tin bệnh án
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    diagnosis = models.TextField()
    treatment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.patient.name}"
