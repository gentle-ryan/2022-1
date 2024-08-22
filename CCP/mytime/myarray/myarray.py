#
# mytime.py
#
# 기말 02 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#

class Vector:
    
    def __init__(self, *vector):
        if type(vector[0]) is list:
            self.vector = tuple(vector[0])
        else:
            self.vector = vector

    def __repr__(self):
        return "Vector{}".format(self.vector)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        return self.vector[index]

    def __setitem__(self, index, value):
        lst = list(self.vector)
        lst[index] = value
        self.vector = tuple(lst)
    
    # 우선, 숫자와의 덧셈과 벡터끼리의 덧셈을 구분었습니다.
    # 숫자와의 덧셈인 경우에는 self.vector의 각 성분에 other만큼을 더하여 새로운 리스트에 추가하도록 하였습니다.
    # 서로 길이가 다른 벡터의 경우에는 길이를 맞추기 위해 길이가 작은 벡터를 길이가 반복하여 새로운 벡터를 만들었습니다.
    # 그 후, 숫자와의 덧셈과동일하게 self.vector의 각 성분에 other.vector의 각 성분을 더했습니다.
    # 곱셈의 경우도 마찬가지로 해결했습니다.
    #

    def __add__(self, other):
        if type(other) is int:
            newvec = []
            for i in range(self.__len__()):
                newvec.append(self.vector[i] + other)
            
            return Vector(newvec)

        else:       
            if self.__len__() > other.__len__():
                rep =  self.__len__() // other.__len__()
                plus = self.__len__() + other.__len__()
                other.vector2 = other.vector * rep + other.vector[:plus:]
                self.vector2 = self.vector

            elif self.__len__() < other.__len__():
                rep =  other.__len__() // self.__len__()
                plus = other.__len__() % self.__len__()
                self.vector2 = self.vector * rep + self.vector[:plus:]
                other.vector2 = other.vector

            newvec = []
            for i in range(self.__len__()):
                newvec.append(self.vector2[i] + other.vector2[i])
            
            return Vector(newvec)


    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) is int:
            newvec = []
            for i in range(self.__len__()):
                newvec.append(self.vector[i] * other)
            
            return Vector(newvec)

        else:       
            if self.__len__() > other.__len__():
                rep =  self.__len__() // other.__len__()
                plus = self.__len__() + other.__len__()
                other.vector2 = other.vector * rep + other.vector[:plus:]
                self.vector2 = self.vector

            elif self.__len__() < other.__len__():
                rep =  other.__len__() // self.__len__()
                plus = other.__len__() % self.__len__()
                self.vector2 = self.vector * rep + self.vector[:plus:]
                other.vector2 = other.vector
            
            newvec = []
            for i in range(self.__len__()):
                newvec.append(self.vector2[i] * other.vector2[i])
            
            return Vector(newvec)
        
    def __rmul__(self, other):
        return self.__mul__(other)

#리스트를 행렬로 예쁘게 표현하는 방법은 구현하지 못하였습니다.

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        matrix = []
        for i in range(row*column):
            matrix.append(float(0))
        self. matrix = matrix

    def __repr__(self):
        return "{}".format(self.matrix)

    def __getitem__(self, index):
        return self.matrix[index[0]-1 + 3*(index[1]-1)]
    
    def __setitem__(self, index, value):
        self.matrix[index[0]-1 + 3*(index[1]-1)] = float(value)
