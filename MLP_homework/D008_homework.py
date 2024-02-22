

def Q1():
    students = [
        {"name": "홍길동", "korean": 87, 'math': 98, "english": 88, "science": 95},
        {"name": "이몽룡", "korean": 92, 'math': 98, "english": 96, "science": 98},
        {"name": "성춘향", "korean": 76, 'math': 96, "english": 94, "science": 90},
        {"name": "변학도", "korean": 98, 'math': 92, "english": 96, "science": 92},
        {"name": "박지성", "korean": 95, 'math': 98, "english": 98, "science": 98},
        {"name": "류현진", "korean": 64, 'math': 88, "english": 92, "science": 92},
    ]
    print(f'이름\t\t총점\t\t평균')
    for data in students:
        data_sum = data['korean'] +data['math'] + data['science'] + data['english']
        print(f"{data['name']}\t{data_sum}\t\t{round(data_sum/4,2)}")

def Q2():
    sampleDictonary = dict()
    while True:
        enterWord = input('영어 단어 등록 (종료는 quit) : ')
        if enterWord == 'quit': break
        elif enterWord in sampleDictonary:
            print(f'{enterWord}는 이미 등록된 단어입니다.')
            continue

        enterMean = input(f'{enterWord}의 뜻 입력 (종료는 quit) : ')
        if enterMean == 'quit': break
        sampleDictonary[enterWord] = enterMean

    print('\n')

    while True:
        searchWord = input('검색할 단어 입력 (종료는 quit) : ')
        if searchWord == 'quit':
            print(f'종료합니다.')
            break
        elif searchWord not in sampleDictonary:
            print(f'{searchWord}는 사전에 없는 단어입니다.\t')
            continue
        print(f'{searchWord}의 뜻은 {sampleDictonary[searchWord]}입니다.\n')

def Q6():
    my_variable = ()

    tmpTuple = 1,

    t = 'a','b','c'
    l_t = list(t)
    l_t[:] = ['A','B','C']
    t = l_t
    print(t)

    interest = ('삼성전자', 'LG전자', 'SK Hynix')
    print(interest)
    interest = list(interest)
    print(interest, type(interest))
    interest = tuple(interest)
    print(interest, type(interest))

    tmpTuple2 = (1, 2, 3)
    tmpTuple2 += 4,
    print(tmpTuple2)

    a = {'A':90, 'B':80, 'C':70}
    a.pop('B')
    print(a)

def Q7():
    partyA = {"Park", "Kim", "Lee"}
    partyB = {"Park", "길동", "몽룡"}

    print("파티에 참석한 모든 사람 : ", partyA.union(partyB))
    print("2개의 파티에 모두 참석한 사람 : ", partyA.intersection(partyB))
    print("파티 A에만 참석한 사람 : ", partyA.difference(partyB))
    print("파티 B에만 참석한 사람:", partyB.difference(partyA))


if __name__ == '__main__':
    Q1()
    print()

    Q2()
    print()

    # Q3.   2 : mutable Type 인 list는 key 값을 기준으로 찾는 dict 타입의 요소로 들어가지 못한다.
    # Q4.   tuple 형식은 요소의 변경이 불가능하다.
    # Q5.   다음의 방식으로는 tuple 의 형태로 바인딩된다.

    Q6()
    print()
    Q7()