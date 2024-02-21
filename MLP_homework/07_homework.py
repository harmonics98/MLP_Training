#2024-02-21
def Q1():
    enterName = None
    l_Name = []
    print(f'회원이름을 입력하세요. 명단을 완성하려면 Q 를 입력하시오.')
    while True:
        enterName = ' ' + input('회원 입력 : ')
        if enterName == ' Q':
            break
        l_Name.append(enterName)

    print(f'회원 명단 : ',end='')
    for i in range(len(l_Name)):
        print(l_Name[i],end='')

def Q2():
    numStudent = int(input('학생 수 입력 : '))
    l_Student = []
    for i in range(numStudent):
        l_Student.append(int(input(f'학생{i+1} 점수 입력 : ')))
    print(f'총점 : {sum(l_Student)} \n평균 : {sum(l_Student)/numStudent}')
    print(f'80점 이상 학생 : {len([student for student in l_Student if student >= 80])}명')
    return l_Student

def Q3():
    enterGoods = None
    l_Goods = []
    while True:
        enterGoods = input('상품 등록 : ')
        if enterGoods == '':
            break
        l_Goods.append(' ' + enterGoods)

    print(f'등록된 상품 : ',end='')
    for i in range(len(l_Goods)):
        print(l_Goods[i],end='')

def Q4():
    l_student = Q2()
    print(f'점수 내림차순 정렬 : {sorted(l_student, reverse=True)}')

def Q5():
    from random import randint
    l_text = ['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
    l_mean = ['잘못을 고치고 옳은 길에 들어섬',
              '죽을 고비를 여러 번 겪으며 살아난다',
              '평범한 사람 가운데 뛰어난 사람',
              '아무짝에나 쓸모 없는 것',
              '고통과 즐거움을 함께 한다',
              '미리 준비해두면 근심 걱정이 없다',
              '사회적으로 인정받고 출세하여 이름을 세상에 드날람',
              '다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
              '생사를 같이 할 수 있는 친밀한 벗',
              '상대 없이 혼자서는 어떤 일을 이룰 수 없다']

    randomQustion = l_mean[randint(0, len(l_text)-1)]
    enterAnswer = None
    print('사자성어 맞추기 게임을 시작합니다\n','-'*30)
    while True:
        print(randomQustion)
        enterAnswer = input('이 말의 사자성어는? : ')
        if enterAnswer in l_text and l_mean[l_text.index(enterAnswer)] == randomQustion:
            print('\n맞습니다.. 게임을 종료합니다.')
            break
        else:
            print('\n틀렸습니다...다시 도전 !\n')

if __name__ == '__main__':
    Q1()
    Q2()
    Q3()
    Q4()
    Q5()