#
# expression.py
#
# 과제06, 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
#
# translate()
# 한글로 사칙연산을 수행하는 함수입니다.
# 연산자는 하나만 허용합니다.
#
# 입력받은 문자열을 분할하여 list 변수를 만들었습니다.
# dictionary를 이용하여 연산자 언어를 기호로 변환하였습니다.
# list의 요소가 operators dict에 존재한다면 value를 result에 추가하여주었습니다.
# 그렇지 않다면, number 모듈에 있는 listen함수를 이용하여 수로 변경하여 result에 추가하였습니다.
# 연산자는 하나만 허용하므로 모든 문장은 숫자-연산자-숫자로 이루어져 있습니다.
# 그렇기에 순서 상관없이 리스트에 추가한 후 문자열로 합쳤습니다.
# 
  
import number

def translate(sentence):
    list = sentence.split()
    operators = {'더하기' : '+', '빼기' : '-', '곱하기' : '*', '나누기' : '/'}
    result = []
    for word in list:
        if word in operators:
            operator = operators[word]
            result.append(operator)
        else:
            num = str(number.listen(word))
            result.append(num)
    result = ' '.join(result)
    return result