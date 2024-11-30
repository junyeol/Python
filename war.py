import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from collections import defaultdict

# 파일 경로 설정
file_path = "Coin.csv"

# 데이터를 저장할 딕셔너리
daily_market_cap = defaultdict(list)

# 파일 읽기
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 헤더 스킵
    header = next(reader)
    
    # 데이터 읽기
    for row in reader:
        # 시간 데이터를 밀리초에서 날짜로 변환
        timestamp_ms = float(row[0])  # 밀리초 단위 시간 데이터
        cap = float(row[1])  # 시가 총액
        
        # 밀리초를 날짜로 변환하여 문자열로 저장
        date_str = datetime.fromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d')
        
        # 날짜 필터링 (2021년 이후)
        if datetime.strptime(date_str, '%Y-%m-%d') >= datetime(2021, 1, 1):
            daily_market_cap[date_str].append(cap)

# 날짜별 평균 계산
snapped_at = []
market_cap = []

for date_str, caps in sorted(daily_market_cap.items()):
    snapped_at.append(datetime.strptime(date_str, '%Y-%m-%d'))
    market_cap.append(sum(caps) / len(caps))  # 평균 계산

# 시각화: 기본적인 꺾은선 그래프
plt.plot(snapped_at, market_cap)

plt.title("Daily Average Market Cap (After 2021)")
plt.xlabel("Date")
plt.ylabel("Average Market Cap (USD)")

# 날짜 형식 및 레이블 간격 설정
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# 로그 스케일 설정 (필요 시)
# plt.yscale('log')

plt.tight_layout()
plt.show()
