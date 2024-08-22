# 
# pysheet.py
#
# 기말01, 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 박유나, 2021-12659 언어학과에 의해 작성되었습니다.
# 
# 
import sys

def autotype(x):
    try:
        val = float(x)
        return val
    except:
        return x

def colnames(filename):
    file = open(filename)
    
    first_line = file.readline()
    colname = first_line.strip().split()
    
    return colname

def subtotal(value_colname, group_colname, filename, calc):
    
    file = open(filename)

    first_line = file.readline()
    colnames = first_line.strip().split()
    
    value_colname_index = colnames.index(value_colname)
    group_colname_index = colnames.index(group_colname)

    total = {}
    count = {}
    for line in file:
        fields = line.strip().split()
        total[fields[group_colname_index]] = total.get(fields[group_colname_index], 0) + float(fields[value_colname_index])
        count[fields[group_colname_index]] = count.get(fields[group_colname_index], 0) + 1

    if calc == 'mean':
        for key in total:
            total[key] = total[key] / count[key]

    subtotals = total
    return subtotals

def colsums(column_range, filename, calc):
    file = open(filename)

    first_line = file.readline()
    colnames = first_line.strip().split()

    first_range = int(column_range[0])
    second_range = int(column_range[2])

    total = {}
    count = 0
    for line in file:
        count += 1
        fields = line.strip().split()
        for i in range(first_range -1 , second_range):
            total[colnames[i]] = total.get(colnames[i], 0) + float(fields[i])
    
    if calc == 'mean':
        for key in total:
            total[key] = total[key] / count

    colsum = total
    return colsum

def table(colname, filename):

    file = open(filename)

    first_line = file.readline()
    colnames = first_line.strip().split()
    
    colname_index = colnames.index(colname)
    
    freq = {}
    for line in file:
        fields = line.strip().split()
        freq[fields[colname_index]] = freq.get(fields[colname_index], 0) + 1

    return freq

def sortby(colname, filename):

    file = open(filename)

    first_line = file.readline()
    colnames = first_line.strip().split()
    
    table = []
    for line in file:
        fields = line.strip().split()
        row = {}
        for i, val in enumerate(fields):
            row[colnames[i]] = autotype(fields[i])
        table.append(row)

    table2 = sorted(table, key=lambda item : item[colname])
    return table2

def frequency(colname, ninterval, filename):
    file = open(filename)

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
    num = (max(table[colname]) - min(table[colname])) / float(ninterval)
    for i in range(int(ninterval) + 1):
        freq['breaks'].append(min(table[colname]) + num*i)

    intervals = freq['breaks']
    for i in range(int(ninterval)):
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
    return freq

def addcol(formula, filename):
    file = open(filename)

    first_line = file.readline()
    colnames = first_line.strip().split()
    
    table = []
    for line in file:
        fields = line.strip().split()
        row = {}
        for i, val in enumerate(fields):
            row[colnames[i]] = autotype(fields[i])
        table.append(row)
    
    first = formula.split()[0]
    second = formula.split()[2]

    for row in table:
            row[formula] = row[first]*row[second]
    
    return table

if __name__ == '__main__':
    command = sys.argv[1]
    
    if command == 'colnames':
        filename = sys.argv[3]
        ans = colnames(filename)

        print(ans) 

    if command == 'subtotal':
        calc = sys.argv[2]
        value_colname = sys.argv[3]
        group_colname = sys.argv[5]
        filename = sys.argv[7]
        
        ans = subtotal(value_colname, group_colname, filename, calc = calc)
        
        for key in ans:
            print(key, ans[key])
    
    if command == 'colsums':
        column_range = sys.argv[2]
        filename = sys.argv[4]
        
        ans = colsums(column_range, filename, calc='sum')

        for key in ans:
            print(key, ans[key])

    if command == 'colmeans':
        column_range = sys.argv[2]
        filename = sys.argv[4]
        
        ans = colsums(column_range, filename, calc='mean')

        for key in ans:
            print(key, ans[key])

    if command == 'table':
        colname = sys.argv[2]
        filename = sys.argv[4]

        ans = table(colname, filename)

        for key in ans:
            print(key, ans[key])

    if command == 'sort':
        colname = sys.argv[3]
        filename = sys.argv[5]

        ans = sortby(colname, filename)
        
        for row in ans:
            values = list(row.values())
            print(*values)
            

    if command == 'frequency':
        colname = sys.argv[2]
        ninterval = sys.argv[3]
        filename = sys.argv[5]
        
        ans = frequency(colname, ninterval, filename)

        for i in range(len(ans['counts'])):
            print(ans['breaks'][i], '-', ans['breaks'][i+1], '|', ans['counts'][i])

    if command == 'hist':
        colname = sys.argv[2]
        ninterval = sys.argv[3]
        filename = sys.argv[5]
        
        ans = frequency(colname, ninterval, filename)
        for i in range(len(ans['counts'])):
            print(ans['breaks'][i], '-', ans['breaks'][i+1], '|', '*' * ans['counts'][i])


    if command == 'addcol':
        formula = sys.argv[2]
        filename = sys.argv[4]
        ans = addcol(formula, filename)

        for row in ans:
            values = list(row.values())
            print(*values)
        





