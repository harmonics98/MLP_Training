

def Part1(): # 선언
    d = dict()
    d1 = {1:'a', 2:'b', 3:'c'}
    print(d1, type(d1))

    d2 = {'name': ['kim', 'hong', 'lee'],
          3 : ['F','C'],
          'gender' : ('m','f')}

    print(d2)

def Part2(): # 조작
    d1 = {1: 'a', 2: 'b', 3: 'c'}

    # 접근
    # print(d1[0]) # KeyError: 0 -> index가 아닌 key 값
    print('d1[1] = ',d1[1])

    # 변경
    d1[1] = 10
    print('After d1[1] = 10, >> ', d1[1])

    # 요소 추가
    d1[4] = 20 # 새로운 key 값
    print('After d1[4] = 20, >> ', d1)

    # 요소 삭제ㅑ
    del d1[4]
    print('After del d1[4], >> ', d1)

def Part3(): # View
    d = {'one':1, 'two':2, 'three':3}
    keys = d.keys()
    print(keys, type(keys))

    values = d.values()
    print(values, type(values))
    print(tuple(values))

    items = d.items()
    print(items, type(items))
    print(list(items))

    for item in d.items():
        print(item, type(item))
    for key, item in d.items():
        print(f'key : {key}, item : {item}')

def Part4(): # method
    d = {'one': 1, 'two': 2, 'three': 3}

    # get()
    print("d.get('two') = ",d.get('two'))
    print("d.get('four') = ",d.get('four'))    # 존재하지 않음. None 반환
    print("d.get('four', 4) = ",d.get('four', 4)) # Key가 없을 때 두번째 인수(4) 반환

    # setdefault()
    print(d)
    d.setdefault('two', 22)
    d.setdefault('four', 4)
    print(d)

    print("d.pop('two') = ", d.pop('two'))
    print("d.popitem() = ", d.popitem())
    print(d)

if __name__ == '__main__':
    # 형식 dict{key(키) : value(값)}
    # key 를 기준으로 접근
    # key 는 중복 불가

    # Part1()
    # Part2()
    # Part3()
    Part4()