list = ["apple", "banana"]
otherlist = ["mango", "cherry", "pineapple"]

def extend(ls,otherls):
    ls += otherls
    return ls
    
result = extend(list, otherlist)
print(result)

