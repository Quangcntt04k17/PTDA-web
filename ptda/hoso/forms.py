from django import forms
from .models import Hoso, BenhAn
from datetime import datetime

class HosoForm(forms.ModelForm):
    class Meta:
        model = Hoso
        fields = ['so_cccd','bhyt', 'ten', 'age','gioi_tinh','sdt', 'dia_chi']
        labels = {
            'so_cccd': 'Số CCCD',
            'bhyt':'Số BHYT',
            'ten': 'Tên',
            'age': 'Tuổi',
            'gioi_tinh': 'Giới tính',
            'sdt': 'SĐT',
            'dia_chi': 'Địa chỉ',
        }
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 1:
            raise forms.ValidationError("Tuổi phải lớn hơn 1.")
        return age



class BenhAnForm(forms.ModelForm):
    ngay_kham = forms.CharField(max_length=10, required=True, label="Ngày khám ")
    
    class Meta:
        model = BenhAn
        fields = ['ma_benh_an', 'ngay_kham', 'khoa_dieu_tri','trieu_chung', 'chuan_doan','dieu_tri', 'so_cccd']
        labels = {
            'ma_benh_an': 'Mã bệnh án',
            'khoa_dieu_tri': 'Khoa điều trị',
            'trieu_chung':'Triệu chứng',
            'chuan_doan': 'Chuẩn đoán',
            'dieu_tri': 'Điều trị',
            'so_cccd': 'Số CCCD',
            
        }
    def clean_ngay_kham(self):
        ngay_kham_str = self.cleaned_data.get('ngay_kham')
        # Danh sách các định dạng ngày tháng hỗ trợ
        date_formats = ['%d/%m/%Y', '%d-%m-%Y']  
        for date_format in date_formats:
            try:
                # Thử chuyển đổi chuỗi thành ngày
                return datetime.strptime(ngay_kham_str, date_format).date()
            except (ValueError, TypeError):
                continue  # Nếu lỗi, thử định dạng tiếp theo
        # Nếu tất cả các định dạng đều không hợp lệ, raise lỗi
        raise forms.ValidationError("Định dạng ngày không hợp lệ. Vui lòng sử dụng 'dd/mm/yyyy' hoặc 'dd-mm-yyyy'.")

    


class FilterBenhAnForm(forms.Form):
    start_date = forms.CharField(max_length=10, required=True, label="Ngày bắt đầu (dd/mm/yyyy)")
    end_date = forms.CharField(max_length=10, required=True, label="Ngày kết thúc (dd/mm/yyyy)")

    def clean_start_date(self):
        start_date_str = self.cleaned_data['start_date']
        return self.parse_date_input(start_date_str)

    def clean_end_date(self):
        end_date_str = self.cleaned_data['end_date']
        return self.parse_date_input(end_date_str)

    def parse_date_input(self, date_str):
        date_formats = ['%d/%m/%Y', '%m/%d/%Y']
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format).date()
            except ValueError:
                continue
        raise forms.ValidationError("Định dạng ngày không hợp lệ. Vui lòng sử dụng 'dd/mm/yyyy' hoặc 'mm/dd/yyyy'.")
