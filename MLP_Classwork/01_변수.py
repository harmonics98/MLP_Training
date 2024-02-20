#Day1 : 변수에 대한 실습


def Swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a,b

def Triangle(w, h):
    print('area : ', (w * h) / 2)

def Part3():
    a = 3
    b = 4
    a, b = Swap(a, b)
    print(a, b)

    # 실습2 : 변수 삭제
    del a
    # print(a)

    # 실습3 : 변수값 출력 print()
    addr = '서울시 서초구'
    name = '아무개'
    age = 24
    result = name + '는 ' + addr + '에 산다'
    print(result)
    # print(name + "의 나이 :" + age) # TypeError : 문자열(str)과 숫자(int)의 결합불가
    print(name + "의 나이 : " + str(age))

def Part5():
    c = 83
    print('넓이 = %f, %i, %d, %s' % (c, c, c, c))
    print('넓이 = %.2f, %5i, %5d, %5s' % (c, c, c, c))
    print(format(c, '.2f'))

    kor = 90;
    eng = 80;
    math = 75
    total = kor + eng + math;
    avg = total / 3
    print('총점 : {0}, 평균 : {1:0.2f}'.format(total, avg))
    print('총점 : {_sum}, 평균 : {_avg:0.2f}'.format(_sum=total, _avg=avg))
    # print('총점 : %d, 평균 : %.2f' %(kor+eng+math, (kor+eng+math)/3))

    # 방식 : '{0:서식} {1:서식} {2:서식}'.format( , , )
    # 방식 : '{value0:서식} {value1:서식} {value2:서식}'.format(value0= , value1= , value2= )
    print(format(3.141592, '6.3f'))
    print('{0:.2f}'.format(3.1415927))

    # 방식 : f'string // f' {value:서식} {value:서식}
    print(f'국어 점수는 {kor:3.1f}점이고, 영어 점수는 {eng:3.1f}')


if __name__ =='__main__':
    # 실습1 : 두 변수의 값 교환(Swap)
    # 실습2 : 변수 삭제 / 실습3 : 변수값 출력 print()
    # Part3()

    # 실습4 : 변수를 이용한 계산 결과값
    # Triangle(10,5)

    # 실습5 : format
    # print( '서식' %값) format string ( %f, %d, %s, %c, %x, %o )
    # Part5()

    # 실습6 : print 활용
    input()
