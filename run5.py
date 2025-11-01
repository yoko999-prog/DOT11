import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import random

URLS = [
    "https://camo.githubusercontent.com/e5d95c97160bf769ddc31bf764e26bf7f75a250f68cec01cc9f3905328bd4509/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d7468616e687475616e787a78266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174",
    "https://camo.githubusercontent.com/893944c5946d6170f13c51d55afa44d29a30dc89c615d61820f8cb12bc25f2f4/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d636f6e6774687563303037266c6162656c3d50726f66696c65253230766965777326636f6c6f723d666630303030267374796c653d666f722d7468652d6261646765",
    # "URL_3",
]
REQUESTS = 10000
CONCURRENCY = 10000

def make_request():
    """Hàm thực hiện một request duy nhất"""
    try:
        # Chọn URL ngẫu nhiên từ danh sách
        url = random.choice(URLS)
        # Gửi request với timeout 3 giây
        requests.get(url, timeout=3)
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
