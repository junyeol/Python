# [데이터 시각화]

import csv
import matplotlib.pyplot as plt
## pip install matplotlib

file_path = "test.csv"

dates = []
temps = []

with open(file_path,mode='r') as file :
    reader = csv.reader(file)

    header = next(reader)

# Alt + 3, 4
##    i = 0
    for row in reader :
        a = row[2]
        b = row[-2]
        if a.startswith("Dec") :
            print(a, b)
            dates.append(a)
            temps.append(float(b))
##            i += 1
##            if i == 10 :
##                break



plt.plot(dates,temps,marker='o',color='r',linestyle=':',linewidth=10,markersize=5)
plt.title("Temperature in December", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.show()

# 과제 1) 막대 그래프로 기온 출력
# 과제 2) 선 그래프 2개를 한 화면에 출력
#       ex) 겨울 최저기온 + 여름 최고기온






            
