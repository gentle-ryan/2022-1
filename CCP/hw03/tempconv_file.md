# tempconv_file: 온도 변환 파일 처리

## 개요

- 섭씨와 화씨 사이의 온도 변화를 하는 모듈을 만든다. `weather` 폴더 아래
  `tempconv.py` 파일 안에 `fahr2cels()`, `cels2fahr()` 함수 작성.
- 실행 파일 `filter.py`를 작성한다.
  - 화씨 온도 데이터가 한 행에 하나씩 들어있는 파일을 IO Redirection을 통해
    표준입력으로 받아들인다.
  - 명령행 인자로 출력하고자 하는 섭씨 온도의 범위를 받는다.
  - 지정된 범위에 해당되는 온도만 섭씨로 변환하여 출력한다.
- 설명을 담고 있는 `README.md` 파일을 작성한다. Markdown 형식을 이용한다.

## 디렉토리 및 파일 

다음과 같이 디렉토리를 구성한다. 전체 디렉토를 압축하여 tempconv_file.zip
파일로 제출한다.

```
tempconv_file/
├── README.md
├── filter.py
├── tempdata_in_fahr.txt
└── weather
    └── tempconv.py
```

## 모듈 import 방법

`filter.py` 파일에서 다음과 같이 `import` 하여 사용할 수 있다.

```python
import weather.tempconv

fahr = 100
cels = weather.tempconv.fahr2cels(fahr)
```

이와 같이 `import`하면 함수 이름이 너무 길어져서 불편할 수 있다. 이름의 충돌이
발생하지 않는 경우에 다음과 같이 사용할 수도 있다.

```python
from weather.tempconv import *

fahr = 100
cels = fahr2cels(fahr)
```

## 프로그램 사용 방법

완성된 `filter.py` 프로그램은 다음과 같은 형식으로 작동해야 한다. 섭씨
$-10$도에서 $-5$도 사이에 해당하는 온도를 변환하여 출력한 것이다. 정확히는
섭씨 온도 $c$ 가 $-10 < c < -5$ 인 경우를 찾아 출력하도록 한다.

```
$ python3 filter.py -10 -5 < tempdata_in_fahr.txt
18.0 -7.777777777777778
22.0 -5.555555555555555
15.0 -9.444444444444445
```

## 추가: 모듈 정보

다음과 같은 명령을 사용하여 모듈에 관한 정보를 얻을 수 있다. 대화형 모드에서
다음 명령들을 실행해 보자.

```python
>>> import math
>>> dir(math)
>>> help(math)
>>> help(math.log)
```

지금 작성한 weather.tempconv 모듈에도 이런 정보를 추가할 수 있다. 다음
명령들을 내려보자.

```
>>> import weather.tempconv
>>> dir(weather.tempconv)
>>> help(weather.tempconv)
```

여기서 `help` 명령을 내렸을 때 다음과 같은 내용이 나오도록 할 수 있다.

```
Help on function cels2fahr in module weather.tempconv:

cels2fahr(cels)
    Convert Celcius to Farenheit
```

이를 위해서는 다음과 같이 파이썬에 docstring이라고 부르는 특별한 형태의 주석을
달아주어야 한다. 따옴표 세 개로 시작하여 따옴표 세 개로 끝나는 문자였다.

```python
def cels2fahr (cels) :
    """Convert Celcius to Farenheit
	""" 
    fahr = cels * 9 / 5 + 32
    return fahr
```





