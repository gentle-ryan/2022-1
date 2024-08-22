#tempconv module 불러오기
import tempconv
from tempconv import fahr2cels, cels2fahr

#화씨->섭씨 변환기  
#매월 1일을 섭씨온도로 변환하기 위한 1의 화씨온도로 구성된 리스트 생성
temp_first = [62, 67, 73, 83, 87, 96, 100, 100, 97, 88, 84, 70]

#for문을 이용하여 temp_first에 있는 각 요소를 화씨온도로 변환하여, 구간에 따라 날씨 설명을 출력하도록 함
print('Fahr to Cels Converter')
for i in temp_first:          
    fahr = float(i)          
    cels = fahr2cels(fahr) 
    if cels >= 30:
        weather = 'hot'
    elif 20 <= cels <30:
        weather = 'warm'
    elif 10 <= cels <20:
        weather = 'mild'
    else:
        weather = 'cool'
    print(i, cels, weather)
print('')
#한달 화씨 기온의 기온 평균, 최소&최대값
print('Average, Minimum and maxium Temperature')
temp_Jan = [62, 68, 64, 66, 72, 64, 65, 64, 60, 63, 66, 68,70, 67, 58, 63, 66,64, 61, 63, 61, 62, 68, 60, 72, 69, 66, 69, 64, 63]

#모듈에 있는 함수를 이용
average_cels = tempconv.average(temp_Jan)
min = tempconv.min(temp_Jan)
max = tempconv.max(temp_Jan)
print("Average Temperature of Janurary :", average_cels)
print("Minimum Temperature of Janurary :", min)
print("Maximum Temperature of Janurary :", max)
print('')

#섭씨->화씨 변환기
print('Cels to Fahr Convertern')
input_cels = float(input("Type Celsius Temp : "))       #데이터가 없기에 입력받을 수 있도록 함
output_fahr = cels2fahr(input_cels)
print("Fahrenheit Temp :", output_fahr)
