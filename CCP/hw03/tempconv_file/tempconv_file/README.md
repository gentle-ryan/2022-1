# 파일 소개
tempconv_file에 있는 모듈과 프로그램을 소개하는 글입니다.
언어학과 2021-12659, 박유나가 작성하였습니다.
# "tempconv.py" 모듈 생성
 
 ```python
 def fahr2cels(fahr):
    """Convert Farenheit to Celcius
	"""
    cels = (fahr - 32) * (5/9)
    return cels

def cels2fahr(cels):
    """Convert Celcius to Farenheit
	"""
    fahr = (cels * 1.8) + 32
    return fahr
```
저번 과제에서 만든 함수를 이용하였다.
help(farh2cels)를 입력하였을 때 합수에 대한 설명이 나오도록 docspring을 활용하여 주석을 달아주었다.

# "filter.py" 프로그램
## 프로그램 소개
filter 프로그램은 화씨 데이터를 입력하면 이를 섭씨데이터로 변환하여, 설정한 범위에 맞는 섭씨 온도만 출력하는 프로그램이다.

## 코드 소개
```python
import sys
from weather.tempconv import cels2fahr
```
프로그램을 작성하기 위해 필요한 모듈과 함수를 불러오는 코드이다.

```python
x1 = int(sys.argv[1])
x2 = int(sys.argv[2])
```
출력할 섭씨온도의 범위를 사용자가 설정하도록 하기 위해 sys.argv를 이용하여 변수를 만들고 int 형식으로 변환해 주었다.

```python
for line in sys.stdin:
    line = float(line)
    cels = fahr2cels(line)
    if x1 < cels < x2:
        print(line, cels)
    else:
        pass
``` 
sys.stdin을 이용하여 이용자가 입력한 데이터에 대하여 결과값을 출력하도록 하였다. 입력받은 데이터는 str 형식이므로 float()를 이용하여 소수로 변환하여준다.
그리고 앞서 만들어 두었던 모듈에 있는 함수인 fahr2cels()를 이용하여 입력받은 화씨 온도를 섭씨온도를 변환해 주었다.
마지막으로 조건문을 이용하여 변환된 섭씨온도가 -10과 -5도 사이인 경우에만 결과값을 출력하도록 하였다.

# additional_filter 프로그램
## 프로그램 소개
cels2fahr()함수를 사용하기 위해 만든 프로그램이다. 섭씨 온도를 화씨온도로 변환 후 정상 체온과 고열, 저체온을 판단하여 메시지를 출력한다.

## 코드 소개
```python
import sys
from weather.tempconv import cels2fahr
```
프로그램을 작성하는데 필요한 모듈과 함수를 불러온다.

```python
print('This is Cels to Fahr Converter and Body Temp Checker.')
print('Please enter the Celcius body temperatures.')
```
이용자로 하여금 어떤 프로그램인지 알 수 있도록하는 안내메세지를 출력하기 위한 코드이다.

```python
for line in sys.stdin:
    line = float(line) 
    fahr = cels2fahr(line) 
    if 95.9 <= fahr <=99: #35.5 ~ 37.2 ℃
        print(line, fahr, "Normal!")
    elif 99 < fahr <= 107.6: #37.2 ~ 42 ℃
        print(line, fahr, "Warning! High")
    elif 91.4 <= fahr < 95.9: #33 ~ 35.5 ℃
        print(line, fahr, "Warning! Low")
    else:
        print("Umm.. It might be not human body temperature..")
```
sys.stdin로 사용자에게 데이터를 입력받도록 하였다. 
입력받은 데이터를  cels2fahr()함수로 화씨 온도로 바꾸어 fahr 변수에 저장하였다.
그 후, 조건문에 따라 체온을 판단할 수 있도록 만들었다.
범위에 따라 정상과 높음, 낮음을 출력하고 높거나 낮은 경우에는 경고메시지를 함께 출력되도록 하였다.
그리고 섭씨로 33~42도의 범위에 있지 않은 온도의 경우에는 사람의 체온이 아닐 것 같다는 문구를 출력하도록 하였다. 