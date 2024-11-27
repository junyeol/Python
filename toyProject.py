## 3번째 일시
## 4번째 평균기온

import csv

file_path = "test.csv"##경로설정

##파일명, 어떤모드로 읽을지, 인코딩, 객체명
with open(file_path,mode='r') as file :
    reader = csv.reader(file)##내장함수아님 csv꺼
    ## 자바에서는 패키지라고한다,파이썬에서는 모듈
    header = next(reader)
     ##for v in 객체(집합명) - 향상된 for문
    for row in reader :
        a = row[2]
        b = row[-2]
        if a.startswith("Dec") :
           print(a, b)
       ##print 한번당 리스트로 나온다
       ##row가 list 타입이라는 사실도 확인가능하다
