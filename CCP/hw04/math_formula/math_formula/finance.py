# finance.py
# 과제04 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#
# rate : interest rate per period
# nper : total number of payment periods in the investment
# pv : present value
#
#function of calculating future value
def fv(rate, nper, pv):
    fv = pv*(1 + rate)**nper
    return fv
