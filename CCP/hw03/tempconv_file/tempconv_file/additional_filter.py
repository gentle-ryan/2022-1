# additional_filter.py
# 과제03 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659, 박유나가 작성하였습니다.

import sys
from weather.tempconv import cels2fahr

print('This is Cels to Fahr Converter and Body Temp Checker.')
print('Please enter the Celcius body temperatures.')
 
for line in sys.stdin:
    line = float(line)
    fahr = cels2fahr(line)
    if 95.9 <= fahr <=99: #35.5 ~ 37.2℃
        print(line, fahr, "Normal!")
    elif 99 < fahr <= 107.6: #37.2~42℃
        print(line, fahr, "Warning! High!")
    elif 91.4 <= fahr < 95.9: #33~35.5℃
        print(line, fahr, "Warning! Low!")
    else:
        print("Umm.. It might be not human body temperature..")
