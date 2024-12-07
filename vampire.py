import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 파일 경로 설정
rainfall_file = "rain.csv"
mosquito_file = "mosquito_data.csv"
temperature_file = "temperature_data.csv"

# 날짜와 강수량, 모기지수, 평균기온 값을 저장할 리스트
dates = []
rainfall_values = []
mosquito_index = []
avg_temp = []

# 강수량 데이터 읽기
with open(rainfall_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        date = datetime.strptime(row[0], "%Y. %m")  # '2016. 05' 형태로 변환
        rainfall = float(row[1])  # 강수량 값을 실수로 변환
        dates.append(date)
        rainfall_values.append(rainfall)

# 모기지수 데이터 읽기
with open(mosquito_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        date = datetime.strptime(row[0].strip(), "%Y-%m-%d")
        mosquito_index.append(float(row[1].strip()))
        # 날짜는 이미 rainfall 데이터와 동일하므로 중복되지 않게 추가할 필요 없음

# 평균 기온 데이터 읽기
with open(temperature_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        try:
            date = datetime.strptime(row[0].strip(), "%Y-%m-%d")
            avg_temp.append(float(row[1].strip()))  # 평균기온
        except ValueError:
            continue  # 변환 실패 시 해당 행 건너뛰기

# 그래프 그리기
plt.figure(figsize=(14, 7))  # 그래프 크기 설정

# 강수량 플롯
plt.plot(dates, rainfall_values, label='Rainfall (mm)', color='blue', linestyle='-', linewidth=2)

# 모기지수 플롯
plt.plot(dates, mosquito_index, label='Mosquito Index', color='green', linestyle='-', linewidth=2)

# 평균 기온 플롯
plt.plot(dates, avg_temp, label='Average Temperature (℃)', color='orange', linestyle='-', linewidth=2)

# 그래프 제목과 축 레이블 설정
plt.title("Rainfall, Mosquito Index & Average Temperature Trends", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Values", fontsize=12)

# x축 레이블 회전 (읽기 쉽도록)
plt.xticks(rotation=45, ha="right")

# 레전드 설정
plt.legend(loc='upper left', fontsize=10)

# 그리드 설정
plt.grid(True, linestyle='--', alpha=0.6)

# 레이아웃 및 출력
plt.tight_layout()
plt.show()
