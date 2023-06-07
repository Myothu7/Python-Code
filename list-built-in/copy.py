list = ["apple", "banana", "mango", "cherry"]

def copy(ls):
    mylist =[]
    mylist += ls
    return mylist

def clear():
    mylist =[]
    return mylist

mylist = copy(list)
print(mylist)

mylist = clear()
print(mylist)