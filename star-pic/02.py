def star(num):
    for i in range(num):
        for j in range(num-i):
            print("*", end='')
        print()

while True:
    num = int(input("Enter number for star pic: "))
    star(num)