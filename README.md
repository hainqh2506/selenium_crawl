# selenium_crawl
bước 1: cài đặt môi trường:
cài đặt python 3.11 và cài thêm selenium bằng câu lệnh: pip install selenium


bước 2: sửa file bot.py để thiết lập trường thông tin cần crawl.
vào file bot.py và chỉnh sửa biến i tương ứng trường dữ liệu cần crawl
    vd: i = 1  #chon i = 
    # 1, Dang ky moi ; 2, Dang ky thay doi ; 3, Thong bao thay doi ; 4,Vi pham / Thu hoi; 5, Giải thể ; 6, Loại khác

    
bước 3: đổi đường dẫn
Đổi đường dẫn tải về trong biến download_path:


bước 4: save

save và chạy file bot.py
---------------------------------------------------------------------------------------------------------------------
 Dưới đây là giải thích ngắn gọn về các bước trong code:

1. Import các thư viện cần thiết:
   - Thư viện `webdriver` từ `selenium` để tạo và điều khiển trình duyệt Chrome.
   - `time` để tạo các khoảng thời gian chờ.

2. Định nghĩa hàm `download_pdf` nhận đầu vào là URL của trang thông tin doanh nghiệp và đường dẫn để lưu trữ các file PDF đã tải xuống.

3. Khởi tạo tùy chọn cho trình duyệt Chrome:
   - Tùy chọn `detach` để tránh đóng trình duyệt sau khi thực thi xong.
   - Vô hiệu hóa thông báo của trình duyệt.
   - Cấu hình đường dẫn download và các tùy chọn liên quan.
   - Có thể sử dụng `headless` để chạy trình duyệt ở chế độ không có giao diện.

4. Khởi tạo trình duyệt Chrome với tùy chọn đã cấu hình.

5. Truy cập vào URL của trang thông tin doanh nghiệp.

6. Chọn mục cần tải xuống:
   - Sử dụng phương thức `find_element` để tìm phần tử mục cần tải xuống dựa trên XPath hoặc CSS Selector.
   - Click vào mục để hiển thị danh sách các file PDF.

7. Tải xuống các file PDF:
   - Sử dụng phương thức `find_element` để tìm phần tử biểu tượng PDF.
   - Sử dụng `execute_script` để thực hiện thao tác click trên biểu tượng PDF.
   - Thời gian chờ 0.1 giây giữa các lần tải xuống để tránh xảy ra lỗi.

8. Lặp lại các bước 6 và 7 cho các trang tiếp theo bằng cách chọn và tải xuống file PDF từ các trang.

9. Kết thúc quá trình và giải phóng tài nguyên.

Lưu ý: Cần đảm bảo trình duyệt Chrome và ChromeDriver đã được cài đặt và cấu hình đúng đường dẫn tới trình duyệt và driver.
