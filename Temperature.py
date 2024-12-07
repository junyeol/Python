import csv
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "CPI.csv"

# 날짜와 CPI 값을 저장할 리스트
dates = []
cpi_values = []

# CSV 파일을 읽어서 데이터 처리
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    # 첫 번째 줄은 헤더이므로 건너뛰기
    next(reader)
    
    # CSV 데이터를 순차적으로 읽으면서 날짜와 CPI 값을 추출
    for row in reader:
        # 첫 번째 열은 '시점', 두 번째 열은 '전국' 데이터 (CPI)
        date = row[0]  # 예: 2010.01, 2010.02 등
        cpi = float(row[1])  # 소비자물가지수 값을 실수로 변환
        
        # 리스트에 날짜와 CPI 값을 추가
        dates.append(date)
        cpi_values.append(cpi)

# 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(dates, cpi_values, color='b', linestyle='-', linewidth=2)

# 그래프 제목과 축 레이블 설정
plt.title("CPI", fontsize=16)
plt.xlabel("date", fontsize=12)
plt.ylabel("CPI", fontsize=12)

# x축 레이블 회전 (읽기 쉽도록)
plt.xticks(rotation=45, ha="right")

# 그래프 표시
plt.tight_layout()
plt.show()
