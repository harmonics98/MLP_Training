def Part1(): # 선언
    t1 = (1,2,3)
    print(t1, type(t1))
    t2 = 4,5,6
    print(t2, type(t2))
    t3 = t1, (7,8,9)
    print(t3, type(t3))
    t4 = [1,2], [3,4,5]
    print(t4, type(t4))
    t5 = tuple([1,2,3])
    print(t5)
    t6 = tuple('hello')
    print(t6)

def Part2(): # 조작
    t = 1,2,3,4,5,6,7
    print('t[5] = ',t[5])
    print('t[:] = ',t[:])
    print('t[::-1] = ',t[::-1])
    print('t * 3 = ',t * 3)
    print(5 in t)

def Part3(): # packing
    t = 1, 2, 'hello'
    x, y, z = t

    print(t, type(t))
    print(x, y, z, type(x), type(y), type(z))

    t2 = 1,2,3,4,5
    a, b, *c = t2
    d, *e, f = t2
    print(a, b, c, type(a), type(b), type(c))
    print(d, e, f, type(d), type(e), type(f))

def Part4(): # 다차원 튜플
    t = ((1,2,3),(4,5,6),(7,8,9))
    print(t)
    for row in t:
        for item in row:
            print(item,' ',end='')
        print()

if __name__ == '__main__':
    # 데이터 값 변경/삭제 불가
    # Part1()
    # Part2()
    # Part3()
    Part4()