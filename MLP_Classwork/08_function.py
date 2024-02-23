def show_list(my_list):
    cpy_list = my_list.copy()
    cpy_list[-1] = 100
    print('cpy_list = ', cpy_list, ' id = ', id(cpy_list))




if __name__ == '__main__':
    my_list = [1,2,3,4]
    print('my_list = ', my_list, ' id = ', id(my_list))
    show_list(my_list)
    print('my_list = ', my_list, ' id = ', id(my_list))
    print((lambda x, *y: x*y)(2,[21,31]))