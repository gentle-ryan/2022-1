import random

def data(name):
    random.seed(name)
    n = 100
    data = []
    for _ in range(n):
        data.append(random.random())
    return data

def text(name):
    random.seed(name)
    n = 1000
    s = ''
    for _ in range(n):
        c = int(random.gauss(70, 30))
        if 32 < c < 127: s += chr(c)
    return s

def abc(name):
    random.seed(name)
    k = random.randint(100, 200)
    s = ''.join(random.choices("|abc", [0.1, 0.2, 0.3, 0.4], k=k))
    return s

def chargram(name):
    random.seed(name)
    freq = [8.2, 1.5, 2.7, 4.7, 13, 2.2, 2, 6.2, 6.9, 0.16, 0.81, 4.0,
            2.7, 6.7, 7.8, 1.9, 0.11, 5.9, 6.2, 9.6, 2.7, 0.97, 2.4, 0.15, 2, 0.078] 
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words = []
    for _ in range(random.randint(1000, 2000)):
        k = max(1, int(random.gauss(5, 2.236)))
        word = ''.join(random.choices(letters, freq, k=k))
        words.append(word)

    s = ' '.join(words)
        
    return s

def csv(name):
    random.seed(name)
    k = random.randint(100, 200)
    numbers = []
    for _ in range(k):
        x = random.randint(10, 100) / 10
        numbers.append(x)
        
    s = ','.join(map(str, numbers))

    return s





