import sys

x = int(sys.argv[1])
y = sys.argv[2]

print(x, y)

file = sys.stdin
for line in file:
    if line == '\n':
        pass
    else:
        print(line, '\n')