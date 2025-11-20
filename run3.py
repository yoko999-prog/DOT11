import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

URL = "https://camo.githubusercontent.com/e5d95c97160bf769ddc31bf764e26bf7f75a250f68cec01cc9f3905328bd4509/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d7468616e687475616e787a78266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174"  # THAY ĐỔI URL
REQUESTS = 10000
CONCURRENCY = 10000

def make_request():
    """Hàm thực hiện một request duy nhất"""
    try:
        # Gửi request với timeout 3 giây
        requests.get(URL, timeout=3)
    except requests.RequestException:
        pass  # Bỏ qua các lỗi nếu có

def send_requests():
    """Hàm thực hiện tất cả requests"""
    # Sử dụng ThreadPoolExecutor để xử lý concurrent requests
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        # Tạo list các task
        futures = [executor.submit(make_request) for _ in range(REQUESTS)]
        # Chờ tất cả các task hoàn thành
        for future in futures:
            future.result()
    print(f"Đã hoàn thành {REQUESTS} requests")

# Vòng lặp vô hạn
while True:
    send_requests()
    time.sleep(1)  # Đợi 1 giây trước khi thực hiện lại
