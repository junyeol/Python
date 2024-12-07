import csv
import matplotlib.pyplot as plt
from datetime import datetime

# CSV 파일 경로
mosquito_file = "mosquito_data.csv"

# 데이터 저장용 리스트
dates = []
mosquito_index = []

# CSV 파일 읽기
with open(mosquito_file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    # 데이터를 리스트로 저장한 뒤 역순 처리
    rows = list(reader)  # 모든 행을 리스트로 저장
    for row in reversed(rows):  # 리스트를 역순으로 읽음
        try:
            # 날짜 변환
            date = datetime.strptime(row[0].strip(), "%Y-%m-%d")
            dates.append(date)

            # 모기지수 저장
            mosquito_index.append(float(row[1].strip()))
        except ValueError:
            print(f"Skipping invalid row: {row}")
            continue  # 변환 실패 시 해당 행 건너뛰기

# 시각화
plt.figure(figsize=(14, 7))

# 모기지수 플롯
plt.plot(dates, mosquito_index, label='Mosquito Index (Residential)', color='green', linewidth=2)

# 그래프 꾸미기
plt.title('Mosquito Index Trends (Past to Recent)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Mosquito Index', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

# 레이아웃 및 출력
plt.tight_layout()
plt.show()
