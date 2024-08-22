# 
# Loop Over List -- Basic Programming Patterns 
#
# 실습01 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다. 
#
# Suppose you are given a list of numbers
import enum


xs = [62, 47, 86, 117, 48, 37, 73, 41, 27, 92, 
      37, 47, 19,  25, 70, 46, 52, 51, 14, 4]


# 1. Summation 
# Compute sum of xs. Do NOT use the built-in function sum()
total = 0
for i in xs:
      total += i

print(total)


# 2. Counting
# How many even numbers in xs?

count = 0
for i in xs:
      count += 1

print(count)

# 3. Searching
# Find the index of 73

search = 73
for i, x in enumerate(xs):
      if x == search:
            index = i
            break
      
print(index)


# 4. Sorting
# Find the maximum. Do NOT use the built-in function max()
maximum = xs[0]
for i in xs:
      if i > maximum:
            maximum = i

print(maximum)

# 5. Mapping 
# Create a list of x*x for all x in xs

squares = []
for i in xs:
      sq = i*i
      squares.append(sq)

print(squares)


# 6. Filtering
# Filter even numbers in xs, i.e. select even numbers from xs
# and create a new list.

evens = []
for i in xs:
      if i % 2 == 0:
            evens.append(i)

print(evens)

