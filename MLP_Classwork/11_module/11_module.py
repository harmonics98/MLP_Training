import modules.packagefile

for i in range(3):
    try:
        print(i, 3// i)
    except ZeroDivisionError:
        print("Not divided by 0")
# if __name__ == "__main__":
#     modules.packagefile.func1()