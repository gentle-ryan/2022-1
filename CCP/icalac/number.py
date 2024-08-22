#
# number.py
#
# 과제06, 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
#
# thousand()
# 1~9999를 한글로 변환하는 함수입니다.
#  
# 한글로 변환할 unit과 nums리스트를 만들었습니다.
# 일의자리부터 시작하여 끝날 때마다 i에 1을 더해 자리수를 변경하여 주었습니다.
# r이 1일 때, 일의 자리를 제외하고는 수를 한글로 표기하지 않기에 조건문으로 작성하였습니다.
# 그 외의 경우에는 nums의 r-1번 요소와 unit의 i번째 요소를 더하여 speak 리스트의 첫번째 자리에 추가하였습니다.
#
# 예를들어, 1021은 다음과 같은 방식으로 작동합니다.
# i = 0, r = 1, n = 102 num = 일
# i = 1, r = 2, n = 10 num = 이 + 십
# i = 2, r = 0, n = 1 pass
# i = 3, r = 1, n = 0 num = 천
# 
  
def thousand(n):
    unit = ['', '십', '백', '천']
    nums = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    speak = []
    i = 0
    while n > 0:
        r = n % 10
        n = int(n / 10)
        if r == 1:
            if i == 0:
                num = nums[r-1] + unit[i]
                speak.insert(0, num)
            else:   
                num = unit[i]
                speak.insert(0, num)
        elif r == 0:
                pass
        else:
            num = nums[r-1] + unit[i]
            speak.insert(0, num)
        i += 1
    return ''.join(speak)

#
# speak()
# 1~999999999999999 까지의 숫자를 한글로 변환하는 함수입니다.
# 
# n이 '영'인 경우는 따로 분류하였습니다.
# 조, 억, 만 단위의 몫과 나머지를 변수로 지정해주었습니다.
# 위에서 작성한 thousand 함수를 이용하여 각각을 한글로 변환하였습니다.
# 각 변수가 비어있지 않다면 단위인 '조', '억', '만'을 추가하여주었습니다.
# 모든 변수를 합쳐 return해 주었습니다.
#
# 예를 들어 200123456은 다음과 같이 작동합니다.
# jo = 0 jo2 = 200123456, uk = 2 uk2 = 123456, man = 12 man2 3456
# num1 = '삼천사백오십육', num2 = '십이', num3 = '이' num4 = ''
# num4 = '', num3 = '이억', num2 = '십이만'
# num = '' + '이억' + '십이만' + '삽천사백오십육'
#

def speak(n):
    if n == 0:
        return '영'
    else:
        jo = int(n / 1000000000000)
        jo2 = n % 1000000000000
        uk = int(jo2 / 100000000)
        uk2 = jo2 % 100000000
        man = int(uk2 / 10000)
        man2 = uk2 % 10000
        num1 = thousand(man2)
        num2 = thousand(man)
        num3 = thousand(uk)
        num4 = thousand(jo)
        if num4 != '':
            num4 = num4 + '조'
        if num3 != '':
            num3 = num3 + '억'
        if num2 != '':
            num2 = num2 + '만'
        num = num4 + num3 + num2 + num1
        return num    

#
# listen()
# 한글로 표현된 숫자를 수로 변환하는 함수입니다.
#
# dictionary를 이용하여 한글을 숫자로 바꾸어주었습니다.
# n이 '영'인 경우는 따로 분류하였습니다.
# 일반 숫자와 단위 숫자를 구분하였습니다. 단위숫자에서는 일,십,백과 만,억,조를 구분하였습니다.
# n을 split으로 분할하여, korea리스트로 만들고 각 요소가 nums, unit1, unit2에 속하는지에 따라 num, unit, big_unit으로 구분하였습니다.
# num은 1~9를 thousand는 10~9999를, total은 10000 이상을 계산합니다.
# 최종적으로 total은 num + thousand + total입니다.
#
# 예를 들어 '칠천오백이억삼천'은 다음과 같은 방식으로 처리됩니다.
# '칠' num = 7, '천' unit = 1000 thousand = 7*1000, num은 0으로 바뀜
# '오' num = 5, '백' unit = 500 thousand = 7500, num은 0으로 바뀜
# '이' num = 2, '억' big_unit = 100000000, total = (7500 + 2) * 100000000, num과 thousand = 0으로 바뀜
# '삼' num = 3, '천' unit = 1000 thousand = 3*1000
# total = total(750200000000) + thousand(3000) + num = 0
# 
 
def listen(n):
    dict = {'일' : 1, '이': 2, '삼' : 3, '사' : 4, '오' : 5, '육': 6, '칠': 7, '팔': 8, '구' : 9, '십' : 10, '백' : 100, '천' : 1000, '만' : 10000, '억' : 100000000, '조' : 1000000000000}
    nums = '일이삼사오육칠팔구'
    unit1 = '십백천'
    unit2 = '만억조' 
    korean = list(n)
    num = 0
    thousand = 0
    total = 0
    if n == '영':
        return 0
    else:
        for ch in korean:
            count = dict.get(ch)
            if ch in nums:
                num = count
            elif ch in unit1:
                unit = count
                if num == 0:
                    num = 1
                    thousand += num*unit
                else:
                    thousand += num*unit
                num = 0
            elif ch in unit2:
                big_unit = count
                if num == 0:
                    num = 1
                    total += (thousand + num) * big_unit
                else: 
                    total += (thousand + num) * big_unit
                thousand = 0
                num = 0
        total = total + thousand + num
    return total                
