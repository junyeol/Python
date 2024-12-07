import csv
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "Stock Market.csv"

# 날짜와 원자료 값을 저장할 리스트
dates = []
values = []

# CSV 파일을 읽어서 데이터 처리
with open(file_path, mode='r') as file:  # 파일을 읽을 때 인코딩을 'utf-8'로 설정
    reader = csv.reader(file)
    
    # 첫 번째 줄은 헤더이므로 건너뛰기
    next(reader)
    
    # CSV 데이터를 순차적으로 읽으면서 날짜와 원자료 값을 추출
    for row in reader:
        # 첫 번째 열은 날짜, 두 번째 열은 원자료
        date = row[0]  # 예: '2010-01-04'
        value = row[1].replace(',', '')  # 쉼표 제거
        
        # 값이 유효한 숫자라면 실수로 변환
        try:
            value = float(value)
        except ValueError:
            value = None  # 변환이 안 되는 값은 None으로 처리
        
        # 리스트에 날짜와 원자료 값을 추가
        dates.append(date)
        values.append(value)

# 연도만 추출
years = [date.split('-')[0] for date in dates]  # '2010-01-04'에서 '2010'만 추출

# 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(dates, values, color='b', linestyle='-', linewidth=2)

# x축 레이블을 연도만 표시하도록 설정
plt.xticks(
    ticks=[i for i in range(len(dates)) if i % 252 == 0],  # 연도별로 한 번만 레이블을 표시 (약 252개 거래일 기준)
    labels=[years[i] for i in range(len(dates)) if i % 252 == 0],  # 해당 인덱스에 해당하는 연도만 레이블로 사용
    rotation=45, ha="right"  # x축 레이블 회전 (읽기 쉽게)
)

# 그래프 제목과 축 레이블 설정
plt.title("Stock Market Value Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Stock Market Value", fontsize=12)

# 그래프 표시
plt.tight_layout()
plt.show()
