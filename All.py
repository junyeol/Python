import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 필터링 기준 날짜
start_date = datetime(2020, 1, 20)
end_date = datetime(2021, 6, 30)

# USD 데이터 읽기
usd_file = "ALL.csv"
dates_usd = []    # 날짜
stocks = []       # 주식 거래량
usd = []          # USD 값

with open(usd_file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        date = datetime.strptime(row[0], "%Y-%m-%d")  # 날짜 형식 변환
        if start_date <= date <= end_date:  # 필터링 조건
            usd_value = float(row[1])  # USD 값
            stock_value = int(row[2])  # 주식 거래량

            dates_usd.append(date)
            usd.append(usd_value)
            stocks.append(stock_value / 1e9)  # 주식 데이터를 10억 단위로 나눔

# USD 데이터 정규화
usd_min, usd_max = min(usd), max(usd)
usd_normalized = [(value - usd_min) / (usd_max - usd_min) * max(stocks) for value in usd]

# CPI 데이터 읽기
cpi_file = "CPI.csv"
dates_cpi = []    # 월별 날짜
cpi_values = []   # CPI 값

with open(cpi_file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        date = datetime.strptime(row[0], "%Y.%m")  # 월별 날짜 형식 변환
        if start_date <= date <= end_date:  # 필터링 조건
            cpi_value = float(row[1])  # CPI 값

            dates_cpi.append(date)
            cpi_values.append(cpi_value)

# 시각화를 위한 그래프 설정
fig, ax1 = plt.subplots(figsize=(14, 7))  # 하나의 그래프를 그리기 위한 subplot 생성

# 첫 번째 y축: 주식 거래량 선 그래프
ax1.plot(dates_usd, stocks, color='tan', label='Stock Market Volume (Billion)', linewidth=2)
ax1.plot(dates_usd, usd_normalized, color='red', label='USD Exchange Rate (Normalized)', linewidth=2)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Volume (Billion) / Normalized USD', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# 두 번째 y축: CPI 데이터 (선 그래프)
ax2 = ax1.twinx()
ax2.plot(dates_cpi, cpi_values, label='CPI', color='blue', linewidth=2)
ax2.set_ylabel('Consumer Price Index (CPI)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# x축 날짜 포맷 및 레이블 설정
plt.xticks(rotation=45)
ax1.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%Y-%m"))
ax1.xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator(interval=3))  # 3개월 간격 표시

# 범례 추가
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# 그래프 제목 및 레이아웃
plt.title("USD, Stock Market Volume, and CPI Trends", fontsize=16)
plt.tight_layout()
plt.show()
