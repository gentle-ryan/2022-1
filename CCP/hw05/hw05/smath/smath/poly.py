# poly.py - polynomials
# 과제05 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#
from math import sqrt
# Polynomial Equation Solver
#
# coefficients : list of coefficients. for example [2, 3, 4] for 2x^2 + 3x + 4
# return list of solutions. for examaple [-1, 1] for x^2 - 1 = 0

def solve(coefficients) :
    if len(coefficients) == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        D = b**2 - 4*a*c
        if a == 0:
                if b != 0:
                    ans = -c / b                    
                    return [ans]
                else:  
                    if c == 0:
                        print("Warning: indeterminate (0/0 form)")
                        return float('nan')
                    else:
                        print("Warning: undefined (there is no possible solution)")
                        return float('nan')
        else:
            if D == 0:
                ans = -b / (2*a)
                return [ans]
            elif D > 0:
                ans1 = (-b + sqrt(D)) / (2*a)
                ans2 = (-b - sqrt(D)) / (2*a)
                return [ans1, ans2]
            else:
                ans1 = complex(-b, sqrt(abs(D))) / (2*a)
                ans2 = complex(-b, -sqrt(abs(D))) / (2*a)
                return [ans1, ans2]

    elif len(coefficients) == 2:
        a = coefficients[0]
        b = coefficients[1]
        if a != 0:
            ans = -b / a
            return [ans]
        else:  
            if b == 0:
                print("Warning: indeterminate (0/0 form)")
                return float('nan')
            else:
                print("Warning: undefined (there is no possible solution)")
                return float('nan')

    elif len(coefficients) == 1:
        print("Warning: undefined (there is no possible solution)")
        return float('nan')
    
    else:
       print("can't solve!", coefficients)
