def Q1():
    for j in range(5, 0, -1):
        for i in range(j, 0, -1):
            print('*',end='')
        print()

def Q2():
    blank = list(range(5, 0, -1))
    star = list(range(1, 11, 2))
    for j, k in zip(blank, star):
        for i in range(j):
            print(' ',end='')
        for i in range(k):
            print('*',end='')
        print()

if __name__ == '__main__':
    Q1()
    Q2()