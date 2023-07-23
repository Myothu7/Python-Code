def star(num):
    for j in range((num - 1) - i):  # space
        print(end=" ")
    for k in range(i):
        print(end=" ")
        print("*", end="")

def pic_between_space(num):
    for j in range(i):  # between pic space
        print(end=" ")
    for k in range(num-i):
        print(end=" ")
        print(" ", end="")

def reverse(num):
    for j in range(i):  # space
        print(end=" ")
    for k in range(num-i):
        print(end=" ")
        print("*", end="")



num = 7
for i in range(1, num):  # total line
    star(num)
    pic_between_space(num)
    star(num)
    pic_between_space(num)
    reverse(num)
    print()

