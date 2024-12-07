import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 파일 경로 설정
file_path = "rain.csv"  # 파일 경로를 실제 CSV 파일로 설정하세요.

# 날짜와 강수량 값을 저장할 리스트
dates = []
rainfall_values = []

# CSV 파일을 읽어서 데이터 처리
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 첫 번째 줄은 헤더이므로 건너뛰기
    next(reader)
    
    # CSV 데이터를 순차적으로 읽으면서 날짜와 강수량 값을 추출
    for row in reader:
        # 첫 번째 열은 '시점', 두 번째 열은 '강수량' 데이터
        date = datetime.strptime(row[0], "%Y. %m")  # '2016. 05' 형태로 변환
        rainfall = float(row[1])  # 강수량 값을 실수로 변환
        
        # 리스트에 날짜와 강수량 값을 추가
        dates.append(date)
        rainfall_values.append(rainfall)

# 그래프 그리기
plt.figure(figsize=(14, 7))  # 그래프 크기 설정
plt.plot(dates, rainfall_values, color='b', linestyle='-', linewidth=2)

# 그래프 제목과 축 레이블 설정
plt.title("Monthly Rainfall (2016-2023)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Rainfall (mm)", fontsize=12)

# x축 레이블 회전 (읽기 쉽도록)
plt.xticks(rotation=45, ha="right")

# 그래프 표시
plt.tight_layout()
plt.show()
