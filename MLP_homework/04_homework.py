def Q1():
    text = input('문자열을 입력하세요 : ')
    print(text.replace('s','$'))

def Q2():
    import datetime
    enterDate = input('날짜(연/월/일) 입력: ')
    lastDate = datetime.datetime.strptime(enterDate,'%Y/%m/%d')+datetime.timedelta(days=3650)
    print(f'입력한 날짜의 10년 후  => {lastDate.year}년{lastDate.month}월{lastDate.day}일')
    del datetime

def Q3():
    nums = input('숫자를 여러개 입력하세요. : ')
    for i in nums:
        print('♥'*int(i))

if __name__ == '__main__':
    # Q1()
    # Q2()
    Q3()