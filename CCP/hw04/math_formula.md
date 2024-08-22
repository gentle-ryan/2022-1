# 수식 구현

다음 문제들을 풀기 위해 필요한 함수들은 지정된 파일에 지정된 함수명을 이용하여
작성하세요. 문제들은 prob01, prob02, prob03 등으로 제시되어 있습니다. 각각의
답을 `return`하는 함수를 `solve.py`라는 파일 안에 `answer01()`, `answer02()`,
`answer03()` 등으로 작성하세요. 모든 파일은 `math_formula`라는 디렉토리 안에
저장하고 디렉토리를 `math_formula.zip` 파일로 압축하여 제출하세요. 제출 방법에
관한 자세한 사항은 마지막에 설명되어 있습니다.

## 뉴턴의 만유인력의 법칙

뉴턴의 만유인력의 법칙은 두 물체 사이의 중력을 기술하는 것이다. 질량이 각각
$m_1$, $m_2$인 두 물체의 중심 사이의 거리가 $r$일 때 두 물체 사이의 중력 $F$는
다음과 같다. 

$$
F = G \frac{m_1 m_2}{r^2} 
$$

여기에서 $G$는 중력 상수로 $6.67408 \times 10^{-11}$이고 이때 단위는
$\text{m}^3 \text{kg}^{-1} \text{s}^{-2}$이다. 힘의 단위는
$\text{kg}\cdot\text{m}\cdot\text{s}^{-2}$이며 간단히 뉴턴(N)이라고도 한다.
중력을 계산하여 주는 함수를 다음과 같은 형식으로 작성하여라. 파일명은
`physics.py`로 하여라.

```python
# mass1 : mass of the object 1 (unit: kg)
# mass2 : mass of the object 2 (unit: kg)
# distance : distance between the centers (unit: m)
def force(mass1, mass2, distance):
```


#### prob01

지구의 무게는 $5.97 \times 10^{24}$ kg이고 달의 무게는 $7.3 \times 10^{22}$
kg이다. 달과 지구 사이의 평균 거리는 $3.84\times 10^8$ m이다. 지구와 달 사이의
중력을 계산하여라.

#### prob02

지구의 적도 반지름은 약 6378km라고 한다. 질량이 240 g인 사과 하나가 나뭇가지에
매달려 있다. 지구와 사과의 사이의 거리를 정확하지는 않지만 6400km라고 하자.
지구와 사과 사이의 중력을 계산하여라.



## 미래 가치

현재 가치를 $\textit{PV}$, 이자율을 $r$, 기간을 $n$이라고 했을 때 미래 가치
$\textit{FV}$는 다음과 같다.

$$
\textit{FV} = \textit{PV}(1 + r)^n
$$

이것을 다음과 같은 함수로 작성하여라. 파일명은 `finance.py`로 하여라. 이것은
Microsfot Excel의 해당 함수를 참조한 형태이다. 실제 Excel의 함수는 조금 더
복잡한 형태이다.

```python
# rate : interest rate per period
# nper : total number of payment periods in the investment
# pv : present value
def fv(rate, nper, pv):
```

1. 이자율 연 2.5%의 연복리로 5년간 1천만원을 정기예금했을 때 이자를 계산하여
   보아라.
2. 이자율 연 2.5%의 월복리로 5년간 1천만원을 정기예금했을 때 이자를 계산하여
   보아라. 즉, 이자율 월 2.5/12 %로 $5 \times 12$ 개월간 정기계금한 것이다.

#### prob03

월복리 이자와 연복리 이자의 차이를 계산하여라.



## 문제와 제출 형식의 예시

이번 과제의 제출을 위한 빈 파일들이 담긴 디렉토리 `math_formula`를 
함께 제공하니 이것을 이용하세요. 

아래는 일반화한 설명입니다. 다음과 같은 과제가 주어졌다고 생각해 봅시다.


> 답을 `return`하는 함수를 `solve.py`라는 파일 안에 `answer01()`,
> `answer02()`, `answer03()` 등으로 작성하여라. 모든 파일은 `homework`라는
> 디렉토리 안에 저장하고 `homework.zip`으로 압축하여 제출하여라.
>
> 다음 함수를 파이썬으로 구현하라. 함수는 `f(x)` 형태로 하고 `my.py`라는
> 파일에 작성하여라.
>
> $$
> f(x) = x + 1
> $$
>
> **(prob01)** 다음 값을 계산하여라.
>
> $$
> f(3)
> $$
>
> **(prob02)** 다음 값을 계산하여라.
>
> $$
> f(10) - f(0)
> $$
> 

이때 `homework`라는 디렉토리 안에 `my.py`와 `solve.py`라는 두 개의 파일이
있어야 합니다. 우선 `my.py` 파일입니다.

```python
# my.py

# add one function
def f(x): 
    return x + 1
```

다음은 `solve.py` 파일입니다.

```python
# solve.py

import my

# calculate f(3)
def answer01():
    ans = my.f(3)
    return ans

# calculate f(10) - f(0)
def answer02():
    ans = my.f(10) - my.f(0)
    return ans
```

