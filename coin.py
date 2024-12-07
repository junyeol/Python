import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from collections import defaultdict

# CSV 데이터 파일 경로
file_path = "Coin.csv"

# 데이터를 저장할 딕셔너리
daily_data = defaultdict(lambda: {"market_cap": [], "total_volume": []})

# 파일 읽기
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 헤더 읽기 및 스킵
    header = next(reader)
    
    # 데이터 읽어서 처리
    for row in reader:
        timestamp_ms = float(row[0])  # 타임스탬프 (밀리초)
        market_cap = float(row[1])    # 시가총액
        total_volume = float(row[2])  # 거래량

        # 타임스탬프를 사람이 읽을 수 있는 날짜로 변환
        date_str = datetime.fromtimestamp(timestamp_ms / 1000).strftime("%Y-%m-%d")
        
        # 날짜별 데이터 저장
        daily_data[date_str]["market_cap"].append(market_cap)
        daily_data[date_str]["total_volume"].append(total_volume)

# 일별 평균 데이터 계산
dates = []
average_market_cap = []
average_total_volume = []

for date_str, data in sorted(daily_data.items()):
    dates.append(datetime.strptime(date_str, "%Y-%m-%d"))
    average_market_cap.append(sum(data["market_cap"]) / len(data["market_cap"]))
    average_total_volume.append(sum(data["total_volume"]) / len(data["total_volume"]))

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 시가총액 그래프
plt.plot(dates, average_market_cap, label="Average Market Cap (USD)", color='b')

# 거래량 그래프
plt.plot(dates, average_total_volume, label="Average Total Volume (USD)", color='g')

# 그래프 제목 및 레이블 설정
plt.title("Daily Market Cap and Total Volume", fontsize=15)
plt.xlabel("Date", fontsize=12)
plt.ylabel("USD", fontsize=12)

# 날짜 포맷 설정 (x축)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# 범례 표시
plt.legend()

# 레이아웃 조정 및 그래프 출력
plt.tight_layout()
plt.show()
