def star_pic(num):
    for i in range(1, num):
        for j in range((num - 1) - i):
            print(end=" ")
        for k in range(i):
            print(end=" ")
            print("*", end="")
        print()
    for i in range(1, num):
        for j in range(i - 1):
            print(end=" ")
        for k in range(num - i):
            print(end=" ")
            print("*", end="")
        print()

while True:
    num = int(input("Enter number: "))
    star_pic(num)


