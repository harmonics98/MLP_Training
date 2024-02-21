def Part1(a):
    a.append('apple')
    a.append('hotdog')
    a.append(10)
    print(a)

def Part2(a):
    value = a.pop()
    print(f'alist : pop data  = {value}, last = {a}')
    a.append('melon')
    print(f'alist : {a}')
    print(f'alist : a.pop(1) = {a.pop(1)}, last = {a}')

def Part3():
    b = [0,1,2]
    print(f'blist {b}')
    b.extend([10,11,12])
    print(f'extend[10,11,12] last = {b}') # 리스트 병합
    b.append([10,11,12])
    print(f'append[10,11,12] last = {b}') # 리스트에 추가
    b.insert(3,[10,11,12])
    print(f'__index=(3, [10,11,12]) last ={b}') # 해당 위치에 요소 추가

def Part4(copy_a):
    cpy_a.clear()   # == cpy_a[:]
    print(f'cpy_a : {cpy_a}')
    
    # del cpy_a   # 메모리 할당 해제

def Part5():
    sampledata = [[90,85,70],[88,79,92],[100,100,100],[90,60,70]]

    print(f'---성적표 (점수)---')
    for data in sampledata:
        print(data)
    print(f'---성적표 (점수, 총점, 평균)---')
    for data in sampledata:
        print(f'{data} {sum(data)}, {(sum(data)/len(data)):.2f}')

if __name__ == "__main__":
    a = []
    Part1(a)
    Part2(a)
    Part3()
    cpy_a = a.copy()
    Part4(cpy_a)
    Part5()