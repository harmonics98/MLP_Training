# time = 10000
# times, second = divmod(time,60)
# hour, minutes = divmod(times,60)
# print(f'{time}초는 {hour}시 {minutes}분 {second}초이다')
#
# b=5
# print(f'{b} : {bin(b)}')
# print(f'{b<<1} : {bin(b<<1)}')
# print(f'{b<<3} : {bin(b<<3)}')

# money = int(input('입력할 지폐 : '))
# ftt, last = divmod(money, 50000)
# ott, last = divmod(last, 10000)
# ft, last = divmod(last,5000)
# t, last = divmod(last,1000)
# print(f'50000원짜리 ==> {ftt}\n10000원짜리 ==> {ott}\n5000원짜리 ==> '
#       f'{ft}\n1000원짜리 ==> {t}\n지폐로 바꾸지 못한 돈 ==> {last}')

# print('등록된 ID : flower')
# print('비밀번호 : 1234')
# id = input('아이디 입력 : ')
# pw = input('비밀번호 입력 : ')
# if id == 'flower' and pw == '1234':
#     print('로그인 성공!')
# else:
#     print('로그인 실패!')

# point = int(input('점수 입력 : '))
# print('grade : ', end='')
# if point >= 90:
#     print('A')
# elif point >= 80:
#     print('B')
# elif point >= 70:
#     print('C')
# elif point >= 60:
#     print('D')
# else:
#     print('F')


if __name__ == "__Main__":
    a = int(input())
    b = int(input())
    print(a+b)

