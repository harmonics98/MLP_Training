def Q1(baseNum):
    if baseNum / 2 == 1:
        return '0b10'
    elif baseNum / 2 == 0:
        return '0b'
    baseNum, remain = divmod(baseNum,2)
    if remain == 1:
        return Q1(baseNum) + '1'
    else:
        return Q1(baseNum) + '0'

def Q2():
    char = input('16진수 한 글자 입력 : ')
    if char in '0123456789abcdefABCDEF':
        char = '0x' + char
        print('10진수 ==> ', int(char,16))
    else:
        print('16진수가 아닙니다.')

if __name__ == '__main__':
    num = int(input('십진수 입력 : '))
    binaryNumber = Q1(num)
    print(binaryNumber)

    Q2()


