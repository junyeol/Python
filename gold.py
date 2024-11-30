import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# 들고올 csv 데이터
file_path = "gold.csv"

# 데이터 배열
dates = []
USD = []

# 파일을 열어서 읽기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)

    # 한줄 먼저 읽어서 수치만 표시
    header = next(reader)

    # 알맞은 값을 배열에 넣기
    for row in reader:
        a = row[0]  # 날짜
        b = row[1]  # USD 값
        print(a, b)

        # 날짜 형식 변환: 문자열을 datetime 객체로 변환
        date_object = datetime.strptime(a, "%Y-%m-%d")
        
        # 배열에 저장
        dates.append(date_object)
        USD.append(float(b))

# 그래프 그리기
plt.plot(dates, USD, color='r')

# 그래프 제목 및 레이블 설정
plt.title("Gold Prices in USD", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("USD", fontsize=10)

# 날짜 포맷 설정 (x축에 날짜가 잘 보이도록)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# 날짜 레이블이 겹치지 않도록 회전시키기
plt.xticks(rotation=45)

# 그래프 표시
plt.show()
