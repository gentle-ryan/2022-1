# filter.py
# 과제03 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659, 박유나가 작성하였습니다.

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
    