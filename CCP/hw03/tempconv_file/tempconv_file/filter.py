# filter.py
# 과제03 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659, 박유나가 작성하였습니다.

import sys
from weather.tempconv import fahr2cels

x1 = int(sys.argv[1])
x2 = int(sys.argv[2])

for line in sys.stdin:
    line = float(line)
    cels = fahr2cels(line)
    if x1 < cels < x2:
        print(line, cels)
    else:
        pass
