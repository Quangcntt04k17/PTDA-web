from django.db import models

# Create your models here.

class BenhNhan(models.Model):

    GIOI_TINH_CHOICES = [
    ('M', 'Nam'),
    ('F', 'Nữ')
]
    maBenhNhan = models.CharField(max_length=10,primary_key=True)
    soCCCD = models.IntegerField(unique=True, null=True, blank=True)
    maBaoHiemYTe = models.IntegerField(unique=True, null=True,blank=True)
    hoTenBenhNhan = models.CharField(max_length=50)
    tuoi = models.IntegerField()
    gioiTinh = models.CharField(max_length=5,choices=GIOI_TINH_CHOICES)  
    soDienThoai = models.IntegerField()
    diaChi = models.CharField(max_length=255)


    def __str__(self):
        return self.hoTenBenhNhan


class BacSi(models.Model):
    GIOI_TINH_CHOICES = [
    ('M', 'Nam'),
    ('F', 'Nữ')
]

    maBacSi = models.CharField(max_length=10,primary_key=True)
    soCCCD=models.IntegerField(unique=True)
    hoTenBacSi = models.CharField(max_length=50)
    tuoi = models.IntegerField()
    gioiTinh = models.CharField(max_length=5,choices=GIOI_TINH_CHOICES)  
    soDienThoai = models.IntegerField()
    diaChi = models.CharField(max_length=255)

    def __str__(self):
        return self.hoTenBacSi


class HoSoBenhAn(models.Model):
    
    maBenhAn = models.CharField(max_length=10,primary_key=True)
    benhNhan = models.ForeignKey(BenhNhan,on_delete=models.CASCADE)
    thoiGianKham = models.DateTimeField(auto_created=True)
    trieuChung = models.CharField(max_length=255)
    chuanDoan = models.CharField(max_length=255)
    dieuTri = models.CharField(max_length=255)
    def __str__(self):
        return f"Hồ sơ bệnh án của {self.benhNhan.hoTenBenhNhan} vào {self.thoiGianKham}"

