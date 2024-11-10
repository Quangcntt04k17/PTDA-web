from django.db import models

class Hoso(models.Model):
    so_cccd = models.CharField(max_length=20, primary_key=True)
    ten = models.CharField(max_length=50)
    bhyt = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    gioi_tinh = models.CharField(max_length=10)
    sdt = models.CharField(max_length=20)
    dia_chi = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.so_cccd

class BenhAn(models.Model):
    ma_benh_an = models.CharField(max_length=10, primary_key=True)
    ngay_kham = models.DateField()
    khoa_dieu_tri = models.CharField(max_length=30)
    trieu_chung = models.CharField(max_length=100)
    chuan_doan = models.CharField(max_length=200)
    dieu_tri = models.CharField(max_length=100)
    so_cccd = models.ForeignKey(Hoso, on_delete=models.CASCADE, to_field='so_cccd')

    def __str__(self):
        return f"{self.ma_benh_an} - {self.chuan_doan}"
