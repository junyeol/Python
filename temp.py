import csv
import matplotlib.pyplot as plt
from datetime import datetime

# CSV 파일 경로
temperature_file = "temperature_data.csv"

# 데이터 저장용 리스트
dates = []
avg_temp = []

# CSV 파일 읽기
with open(temperature_file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        try:
            # 날짜 변환
            date = datetime.strptime(row[0].strip(), "%Y-%m-%d")
            dates.append(date)

            # 평균 기온 저장
            avg_temp.append(float(row[1].strip()))  # 평균기온
        except ValueError:
            print(f"Skipping invalid row: {row}")
            continue  # 변환 실패 시 해당 행 건너뛰기

# 시각화
plt.figure(figsize=(14, 7))

# 평균 기온
plt.plot(dates, avg_temp, label='Average Temperature (℃)', color='orange', linewidth=2)

# 그래프 꾸미기
plt.title('Average Temperature Trends', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (℃)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

# 레이아웃 및 출력
plt.tight_layout()
plt.show()
