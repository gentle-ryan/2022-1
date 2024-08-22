#
# mytime.py
#
# 실습 09 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#

class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__total_seconds = s = hours * 3600 + minutes * 60 + seconds
        
        hours = int(s // 3600)
        s = (s - hours * 3600)
        minutes = int(s // 60)
        seconds = float(s - minutes * 60)

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return "Time ({}, {}, {})".format(self.hours, self.minutes, self.seconds)

    def total_seconds(self):
        return self.__total_seconds
    
    def __add__(self, other):
        s = self.total_seconds() + other.total_seconds()
        return Time(seconds = s)
    
    def __sub__(self, other):
        s = self.total_seconds() -other.total_seconds()
        return Time(seconds = s)
    
    def __mul__(self, x):
        s = x * self.total_seconds()
        return Time(seconds =s)
    
    def __rmul__(self, x): # x * t1
        return self.__mul__(x)
    
    def __lt__(self, other):
        return self.total_seconds() < other.total_seconds()

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()
