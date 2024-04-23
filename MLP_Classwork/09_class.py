
class Dog:
    def __init__(self, name, breed, size, age, color):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.Color = color

    def eat(self, food):
        print(f'{self.name}이 {food}를 먹는다.')

    def sleep(self):
        print(f'{self.name}이 잠잔다')

    def sit(self):
        print(f'{self.name}이 앉아있다.')

    def run(self):
        print(f'{self.name}이 뛴다.')

class Product():
    pass

class Inventory():
    def __init__(self):
        self.__items = []

    def addNewItem(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberOfItems(self):
        return len(self.__items)

class Person:
    pass



if __name__ == '__main__':
    dogA = Dog('삐삐','Maltese','small',2,"while")
    dogB = Dog('벤','Chow Chow','medium', 3, 'brown')
    dogC = Dog('뭉치','Mastiff', 'large', 5, 'black')
