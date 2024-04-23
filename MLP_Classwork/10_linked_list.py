class Node():
    def __init__(self):
        self.data = None
        self.link = None




if __name__ == '__main__':
    node1 = Node()
    node1.data = '다현'

    node2 = Node()
    node2.data = '정현'

    node1.link = node2
    head = node1

    print(head.link.data)



## 권장 자격증
# - 정보처리기사, 전자계산기조직응용.