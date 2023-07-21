def star_pic(num):
    for i in range(num):
        for j in range(2+(2*i)):
            print("*", end='')
        print()

while True:
    num = int(input("Enter number for star pic: "))
    star_pic(num)