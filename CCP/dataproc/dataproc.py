#
# dataproc.py - data processing exercise
#
# 실습 06 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.

# (Example 3.2)
# sum numbers in numbers.txt
#

file = open("data/numbers.txt")

total = 0
for line in file:
    x = float(line)
    total += x

file.close()

print(total)

# (Example 3.8)
# sum numbers in mat.txt
#

file = open("data/mat.txt")

total = 0
for line in file:
    toks = line.split()
    for tok in toks:
        x = float(tok)
        total += x

file.close()

print(total)

#
# sum the 3rd column in table.txt
#

file = open("data/table.txt")
  
firstline= file.readline()
colnames = firstline.split()

for line in file:
    name, qty, mrp = line.split()
    mrp = float(mrp)
    print(mrp)
    total += mrp

file.close()

print(colnames[2], total)

#
# row sums in mat.txt
#

file = open("data/mat.txt")

rowsums = []
for line in file:
    toks = line.split()
    total = 0.0
    for tok in toks:
        x = float(tok)
        total += x
    
    rowsums.append(total)
    
file.close()

print(rowsums)

#
# count g's in dna
#
dna = 'gtgcgactccttctatgagtagaccacacctt'

count = 0
for base in dna:
    if base == 'g':
        count += 1

print(count)

#
# count apple's in names.txt
#

file = open("data/names.txt")

count = 0
for line in file:
    word = line.strip() # delete \n
    if word == 'apple':
        count += 1

file.close()

print(count)


#
# count apple's in text.txt
#

file = open("data/text.txt")

count = 0
for line in file:
    words = line.split()
    for word in words:
        if word == 'apple':
            count += 1

file.close()

print(count)
    
#
# compute letter frequency in dna.txt
#

# method 1
file = open("data/dna.txt")
countG = 0
countC = 0
countT = 0
countA = 0
counts = []

for line in file:
    words = line.split()
    for word in words:
        for letter in word:
            if letter == 'g':
                countG += 1           
            elif letter == 'c':
                countC += 1
            elif letter == 't':
                countT += 1
            else:
                countA += 1
counts.append(countG)
counts.append(countC)
counts.append(countT)
counts.append(countA)


file.close()
print(counts)

# 처음에는 이렇게 작성하였으나 변수가 너무 많고 append문이나 조건문이 반복되는 것 같아 고민을 하였습니다.

# method 2

file = open("data/dna.txt")
letters = []
freq = []
for line in file:
    for word in line:
        letter = word.strip()
        print(letter)
        if letter in letters:
            pass
        elif letter == '':
            pass
        else:
            letters.append(letter)
            freq.append(0)
        for i in range(len(letters)):
            if letters[i] == letter:
                    freq[i] += 1

for i in range(len(letters)):
    print(letters[i], ":", freq[i])

# 각 철자의 개수와 빈도의 가지수는 같으니, 각각의 list를 만들고 조건문과 반복문을 이용하여 추가하여 주었습니다.
