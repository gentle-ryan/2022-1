#화씨->섭씨 변환 함수
def fahr2cels(x):
    y = (x - 32) * (5/9)
    return y

#섭씨->화씨 변환 함수
def cels2fahr(x):
    y = (x * 1.8) + 32
    return y

#sum(), min(), max() 함수를 이용할 수 있었지만 모듈 불러오는 연습을 위해 만들어 사용
#평균 구하는 함수
def average(x):
    sum = 0             
    for i in x:
        sum += i
    average = sum / len(x)
    return average

#최솟값 구하는 함수
def min(x):             
    min = x[0]
    for i in x:
        if i<=min:
            min= i
    return min

#최댓값 구하는 함수
def max(x):
    max = x[0]
    for i in x:
        if i>=max:
            max= i
    return max
