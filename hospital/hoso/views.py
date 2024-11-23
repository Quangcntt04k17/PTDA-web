from .models import BenhNhan, BacSi,HoSoBenhAn
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BenhNhanSerializer
from .serializers import HoSoBenhAnSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError



class DanhSachHosoView(APIView):
    def get(self, request):
        # Lấy danh sách hồ sơ từ database
        danh_sach_hs = BenhNhan.objects.all()
        
        # Sử dụng serializer để chuyển đổi dữ liệu thành định dạng JSON
        serializer = BenhNhanSerializer(danh_sach_hs, many=True)
        
        # Trả về dữ liệu dưới dạng JSON
        return Response({'danh_sach_hs': serializer.data}, status=200)






class DanhSachBenhAnView(APIView):
    def get(self, request):
        # Lấy tất cả các bệnh án
        benh_an_list = HoSoBenhAn.objects.all().order_by('-thoiGianKham')  # Sắp xếp theo ngày khám mới nhất
        
        # Nếu bạn muốn lọc theo số CCCD thì dùng đoạn mã dưới
        # so_cccd = request.GET.get('so_cccd', None)
        # if so_cccd:
        #     benh_an_list = benh_an_list.filter(so_cccd__so_cccd=so_cccd)

        # Serialize dữ liệu để trả về
        serializer = HoSoBenhAnSerializer(benh_an_list, many=True)
        return Response({'benh_an': serializer.data}, status=status.HTTP_200_OK)
    
    
class ThemHosoView(APIView):
    
    def post(self, request):
        # In ra dữ liệu nhận được để kiểm tra
        print("Received data:", request.data)

        # Chuyển dữ liệu từ request thành serializer để kiểm tra tính hợp lệ
        serializer = HoSoBenhAnSerializer(data=request.data)
        
        if serializer.is_valid():
            # Nếu dữ liệu hợp lệ, lưu bệnh án và trả về phản hồi thành công
            serializer.save()
            return Response({'message': 'Thêm bệnh án thành công!'}, status=status.HTTP_201_CREATED)
        else:
            # Nếu dữ liệu không hợp lệ, trả về lỗi
            print("Validation errors:", serializer.errors)
            raise ValidationError({'errors': serializer.errors})


class ThemBenhAnView(APIView):
# {
#     "maBenhAn": "BA12345678",
#     "benhNhan": "1234567890",
#     "thoiGianKham": "2024-11-23T10:00:00Z",
#     "trieuChung": "Ho, sốt, đau họng",
#     "chuanDoan": "Viêm phổi",
#     "dieuTri": "Uống thuốc kháng sinh"
# }

    def post(self, request):
        # Lấy dữ liệu từ request
        data = request.data

        # Kiểm tra xem bệnh nhân có tồn tại không
        try:
            benhnhan = BenhNhan.objects.get(soCCCD=data['soCCCD'])
        except BenhNhan.DoesNotExist:
            raise ValidationError("Bệnh nhân không tồn tại!")

        # Kiểm tra nếu mã bệnh án đã tồn tại
        if HoSoBenhAn.objects.filter(maBenhAn=data['maBenhAn']).exists():
            return Response({"detail": "Mã bệnh án đã tồn tại!"}, status=status.HTTP_400_BAD_REQUEST)

        # Khởi tạo serializer với dữ liệu
        serializer = HoSoBenhAnSerializer(data=data)

        # Kiểm tra xem serializer có hợp lệ không
        if serializer.is_valid():
            # Lưu bệnh án và liên kết với bệnh nhân
            serializer.save(soCCCD=benhnhan)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TimKiemCCCDView(APIView):
    def get(self, request):
        # Lấy giá trị số CCCD từ tham số truy vấn
        so_cccd = request.GET.get('soCCCD', None)
        
        if so_cccd is None:
            return Response({'error': 'Vui lòng cung cấp số CCCD.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Lọc bệnh án theo số CCCD của bệnh nhân
        benh_an_list = HoSoBenhAn.objects.filter(benhNhan__soCCCD=so_cccd).order_by('-thoiGianKham')
        
        if not benh_an_list.exists():
            return Response({'message': 'Không tìm thấy bệnh án nào cho số CCCD này.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize dữ liệu và trả về kết quả
        serializer = HoSoBenhAnSerializer(benh_an_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
from .forms import FilterBenhAnForm  # Import form nếu cần sử dụng trong view
class LocBenhAnView(APIView):
    # http://127.0.0.1:8000/api/hoso/loc/?start_date=2024-01-01&end_date=2024-11-23
    def get(self, request):
        # Lấy dữ liệu từ GET request
        form = FilterBenhAnForm(request.GET)

        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            # Lọc bệnh án theo khoảng thời gian
            danh_sach_benh_an = HoSoBenhAn.objects.filter(thoiGianKham__range=(start_date, end_date)).order_by('-thoiGianKham')
            
            # Serialize dữ liệu bệnh án
            benh_an_data = HoSoBenhAnSerializer(danh_sach_benh_an, many=True).data

            return Response({
                'danh_sach_benh_an': benh_an_data
            }, status=status.HTTP_200_OK)

        return Response({
            'errors': form.errors
        }, status=status.HTTP_400_BAD_REQUEST)
