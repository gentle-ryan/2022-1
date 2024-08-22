from audioop import ratecv
from curses import has_extended_color_support


file = open("sales.txt")

first_line = file.readline()
colnames = first_line.strip().split()

total = {}
for line in file:
    name, year, amount = line.strip().split()
    amount = float(amount)
    total[name] = total.get(name, 0) + amount

print(total)

value_colname_index = colnames.index('amount')
group_colname_index = colnames.index('name')

total = {}
for line in file:
    fields = line.strip().split()
    total[fields[group_colname_index]] = total.get(fields[group_colname_index], 0) + float(fields[value_colname_index])

for key in total:
    print(key, total[key])

file = open("emp.dat")

first_line = file.readline()
colnames = first_line.strip().split()
    
table = []
for line in file:
    fields = line.strip().split()
    row = {}
    for i, val in enumerate(fields):
        row[colnames[i]] = autotype(fields[i])
    table.append(row)

colname = 'age'

table2 = sorted(table, key=lambda item : item[colname])
table2








first_line = file.readline()
colnames = first_line.strip().split()
column_range = '2-4'

first_range = int(column_range[0])
second_range = int(column_range[2])

total = {}
count = 0
for line in file:
    count += 1
    fields = line.strip().split()
    for i in range(first_range, second_range + 1):
        total[colnames[i]] = total.get(colnames[i], 0) + float(fields[i])
    

for key in total:
    print(key, total[key])


if calc == 'mean':
    for key in total:
        total[key] = total[key] / count

total = {}
count = 0
for line in file:
    count += 1
    fields = line.strip().split()
    for i in range(1, 4):
        total[colnames[i]] = total.get(colnames[i], 0) + float(fields[i])

for key in total:
    print(key, total[key])

def autotype(x):
    try:
        val = float(x)
        return val
    except:
        return x

file = open("class.txt")

first_line = file.readline()
colnames = first_line.strip().split()

table = {}

for line in file:
    fields = line.strip().split()
    for i, val in enumerate(fields):
        if colnames[i] in table:
            table[colnames[i]].append(autotype(val))
        else:
            table[colnames[i]] = []
            table[colnames[i]].append(autotype(val))

for key in table:
    print(key, table[key])

print(table)


file = open('emp.dat')

colname = 'rate'
ninterval = 5

first_line = file.readline()
colnames = first_line.strip().split()

table = {}
for line in file:
    fields = line.strip().split()
    for i, val in enumerate(fields):
        if colnames[i] in table:
            table[colnames[i]].append(autotype(val))
        else:
            table[colnames[i]] = []
            table[colnames[i]].append(autotype(val))

freq = {'breaks':[], 'counts':[]}
num = (max(table[colname]) - min(table[colname])) / ninterval
for i in range(ninterval + 1):
    freq['breaks'].append(min(table[colname]) + num*i)

intervals = freq['breaks']
for i in range(ninterval):
    freq['counts'].append(0)

for val in table[colname]:
    for i in range(len(intervals)):
        if i == 0:
            if intervals[i] <= val <= intervals[i+1]:
                freq['counts'][i] += 1
        elif i == 5:
            pass
        else:
            if intervals[i] < val <= intervals[i+1]:
                freq['counts'][i] += 1

for i in range(len(freq['counts'])):
    print(freq['breaks'][i], '-', freq['breaks'][i+1], '|', freq['counts'][i])

for i in range(len(freq['counts'])):
    print(freq['breaks'][i], '-', freq['breaks'][i+1], '|', '*' * freq['counts'][i])

file = open("emp.dat")

def autotype(x):
    try:
        val = float(x)
        return val
    except:
        return x


first_line = file.readline()
colnames = first_line.strip().split()

table = []
for line in file:
    fields = line.strip().split()
    row = {}
    for i, val in enumerate(fields):
        row[colnames[i]] = autotype(fields[i])
    table.append(row)

formula = 'hour * 60'
first = formula.split()[0]
globals()[first] = 'hour'
exec(first) = hour
hour

eval(formula)

second = formula.split()[2]
type(second)

for row in table:
    if first in row:
        formula.split()[0] = row[first]
    if second in row:
        second = formula.split()[2] = row[second]
    print(eval(formula))

'rate' in table