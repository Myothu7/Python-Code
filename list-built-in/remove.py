mylist = ["green", "blue", "red", "cyan"]

def remove(list,value):
    newls = []
    for a in list:
        if(a != value):
            newls += [a] 
    return newls

mylist = remove(mylist,"blue")
print("Remove list: ",mylist)