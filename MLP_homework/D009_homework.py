# 1.  Before: 10
#     In function: 20
#     After:: 10
# 2.  None
# 3.  Error
# 4.  False
# 5.  Error
# 6. ['green', 'blue']
# 7.  8
#     None
# 8. ['appl']
# 9.  I Love You543210
# 10. ['x']
# 11. Odd
#     Even
#     repeat
# 12. Value:10
#     Value:20
# 13. A
#     B
#     C
#     A
#     B
# 14. A
#     A
#     C
#     B
# 15. B
#     A
# 16. A
#     C
#     B
#     E
#     D
# 17. B
#     C
#     B
#     C
#     B
#     C
#     A
# 18. 출력 없음
# 19. None

# def factorial_calculator(n):
#     if n in (0, 1):
#         return 1
#     else:
#         return n * factorial_calculator(n-1)
# print(factorial_calculator(5))

# 2. factorial_calculator(n-1)
# 3. 함수를 읽어서 메모리에 저장되기 전에 함수를 호출하고 있음.

def print_coin():
    print('"비트코인"')

def print_coins():
    for i in range(100):
        print_coin()
def mul(num1, num2):
    return num1*num2

def toUpper(text):
    return text.upper()

pickup_even = lambda picked_list:[picked_list[i] for i in range(len(picked_list)) if i % 2 != 0]

if __name__ == '__main__':
    print_coin()
    for i in range(100): print_coin()



