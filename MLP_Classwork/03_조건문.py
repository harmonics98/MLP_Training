def Part1():
    enterNum = int(input('정수 입력 : '))
    if enterNum % 2 == 0:
        print('짝수')
    else:
        print('홀수')

def Part2():
    enterNum1, enterNum2, enterNum3 = map(int,input('정수 입력 : ').split())
    if enterNum1 < enterNum2:
        if enterNum2 < enterNum3:
            topNum = enterNum3
        else:
            topNum = enterNum2
    else:
        if enterNum1 < enterNum3:
            topNum = enterNum3
        else:
            topNum = enterNum1
    # topNum = max(enterNum1,enterNum2,enterNum3)
    print(topNum)

def Part3():
    enterShape = input('(1: 사각형, 2: 삼각형 3: 원) :')
    if enterShape == '3':
        radius = float(input('반지름 : '))
        print('원의 면적 = ', pow(radius, 2) * 3.14)
    else:
        enterW, enterH = map(float, input('가로 세로 : '.split()))
        if enterShape == '1':
            print('사각형의 면적 = ', enterH * enterW)
        elif enterShape == '2':
            print('삼각형의 면적 = ', enterH * enterW / 2)

def Part4():
    import random
    # del random
    humanNum = int(input('주사위 눈의 수 입력 : '))
    comNum = random.randint(1,6)
    if humanNum > comNum:
        print('승리')
    elif humanNum == comNum:
        print('비김')
    else:
        print('패배')
    del random


def Part5():
    total = 0
    start, end = map(int,input().split())
    for num in range(start,end):
        total += num
    print(total)

def Part6():
    for i in range(0,9,4):
        for j in range(1,5):
            print(i+j,'\t',end='')
        print()

def Part7():
    num = int(input('숫자 입력 : '))
    while num != 7:
        num = int(input('다시 입력 : '))
    print('7 입력. 종료')

def Part8():
    nums = []
    count_plus=count_minus=count_zero=0
    for i in range(10):
        num = float(input(f'숫자{i+1}입력 : '))
        nums.append(num)
        if num > 0: count_plus+=1
        elif num < 0: count_minus+=1
        else: count_zero+=1
    print(f'양의 개수 : {count_plus}')
    print(f'음의 개수 : {count_minus}')
    print(f'0의 개수 : {count_zero}')

def Part9():
    nums = []
    count_plus = count_minus = count_zero = 0
    i=1
    while i < 11:
        num = float(input(f'숫자{i}입력 : '))
        nums.append(num)
        if num > 0:
            count_plus += 1
        elif num < 0:
            count_minus += 1
        else:
            count_zero += 1
        i += 1
    print(f'양의 개수 : {count_plus}')
    print(f'음의 개수 : {count_minus}')
    print(f'0의 개수 : {count_zero}')

if __name__ == '__main__':
    # Part1()
    # Part2()
    # Part3()
    # Part4()
    # Part5()
    # Part6()
    # Part7()
    # Part8()
    # Part9()
    Part10()